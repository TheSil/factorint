import logging
import sys
from enum import Enum
from typing import List

from factorint.baillie_psw import check_prime_baillie_psw
from factorint.exception import FactorException
from factorint.pollard_rho import find_by_pollard_rho
from factorint.small_primes import small_primes
from factorint.state import FactorComponent, FactorizationState
from factorint.utils import get_perfect_power, isqrt

logger = logging.getLogger("factorint")
logging.basicConfig(stream=sys.stdout, level=logging.WARNING)


class NoFactorFound(FactorException):
    pass


class NoFullFactorizationFound(FactorException):
    pass


def check_perfect_power(state: FactorizationState) -> bool:
    n = state.to_factor.base
    base, exp = get_perfect_power(n)
    if exp != 1:
        state.add_divisor(base)
        return True

    return False


def find_small_prime_factor(state: FactorizationState) -> bool:
    n = state.to_factor.base
    start_n = n
    sqrt_n = isqrt(n)
    for p in small_primes:
        if n % p == 0:
            state.add_prime_factor(p)
            n = state.to_factor.base
            sqrt_n = isqrt(n)
            if n == 1:
                break

        state.primes_checked_up_to = p

        if p > sqrt_n:
            state.primes_checked_up_to = n
            state.add_prime_factor(n)
            return True

    return start_n != n


class FactorizationMode(Enum):
    FullFactorization = 1
    PartialFactorization = 2
    FirstFactor = 3


def factor(n, mode: FactorizationMode = FactorizationMode.FullFactorization, verbose=False) -> List[FactorComponent]:
    state = FactorizationState(n)
    algs = [check_perfect_power,
            check_prime_baillie_psw,
            find_by_pollard_rho]

    if verbose:
        logger.setLevel(logging.INFO)

    logger.log(logging.INFO, f"factoring: {n}")
    logger.log(logging.INFO, f"checking for small prime factors")

    # small primes are special, we need to check them only once
    state.to_factor = state.to_factor_comps.get()
    find_small_prime_factor(state)

    if mode == FactorizationMode.FirstFactor and state.prime_comps:
        return state.prime_comps

    if state.to_factor.base != 1:
        state.to_factor_comps.put(state.to_factor)
        state.to_factor = None

    while not state.to_factor_comps.empty():
        state.to_factor = state.to_factor_comps.get()
        prev = state.to_factor.base

        logger.log(logging.INFO, f"checking factor: {state.to_factor.base}")

        for alg in algs:
            logger.log(logging.INFO, f"running alg: {alg.__name__}")

            while alg(state):
                if state.to_factor.base == 1:
                    break
                if state.to_factor.base != prev and mode == FactorizationMode.FirstFactor:
                    break

            if state.to_factor.base != prev:
                break

        if state.to_factor.base == prev:
            state.unfactored.append(state.to_factor)
            state.to_factor = state.to_factor_comps.get() if not state.to_factor_comps.empty() else None
        elif state.to_factor.base != 1:
            # something unfactored still remains, push to trough the pipeline
            state.to_factor_comps.put(state.to_factor)

        if mode == FactorizationMode.FirstFactor and state.prime_comps:
            return state.prime_comps

    logger.log(logging.INFO, f"found prime factors: {state.prime_comps}")
    logger.log(logging.INFO, f"remaining factors: {state.unfactored}")
    logger.log(logging.INFO, f"checked all primes up to: {state.primes_checked_up_to}")

    if not state.unfactored:
        return state.prime_comps

    if mode == FactorizationMode.FirstFactor:
        raise NoFactorFound()

    if mode == FactorizationMode.PartialFactorization:
        if state.prime_comps:
            return state.prime_comps + state.unfactored
        raise NoFactorFound()

    raise NoFullFactorizationFound()
