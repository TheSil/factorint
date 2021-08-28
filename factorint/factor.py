from enum import Enum
from typing import List

from .exception import FactorException
from .pollard_rho import find_by_pollard_rho
from .small_primes import find_small_prime_factor
from .state import FactorComponent, FactorizationState
from .utils import get_perfect_power
from .wheel_factorization import find_by_wheel_division


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


class FactorizationMode(Enum):
    FullFactorization = 1
    PartialFactorization = 2
    FirstFactor = 3


def factor(n, mode: FactorizationMode = FactorizationMode.FullFactorization, verbose=False) -> List[FactorComponent]:
    state = FactorizationState(n)
    algs = [check_perfect_power,
            find_small_prime_factor,
            find_by_wheel_division,
            find_by_pollard_rho]

    while not state.to_factor_comps.empty():
        state.to_factor = state.to_factor_comps.get()
        if verbose:
            print(f"factoring: {state.to_factor.base}")
        for alg in algs:
            if verbose:
                print(f"running alg: {alg.__name__}")
            while alg(state):
                if state.to_factor.base == 1 or \
                        mode == FactorizationMode.FirstFactor:
                    break

            if state.to_factor.base == 1 or \
                    mode == FactorizationMode.FirstFactor:
                break

        if state.to_factor.base != 1:
            state.unfactored.append(state.to_factor)

        if mode == FactorizationMode.FirstFactor and state.prime_comps:
            return state.prime_comps

    if verbose:
        print(f"found prime factors: {state.prime_comps}")
        print(f"remaining factors: {state.unfactored}")
        print(f"checked all primes up to: {state.factored_to}")

    if not state.unfactored:
        return state.prime_comps

    if mode == FactorizationMode.FirstFactor:
        raise NoFactorFound()

    if mode == FactorizationMode.PartialFactorization:
        if state.prime_comps:
            return state.prime_comps
        raise NoFactorFound()

    raise NoFullFactorizationFound()

