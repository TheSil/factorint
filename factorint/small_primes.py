import math

from .eratosthenes import sieve_of_eratosthenes
from .state import FactorizationState

small_primes = sieve_of_eratosthenes(10000)


def find_small_prime_factor(state: FactorizationState) -> bool:
    n = state.to_factor.base
    sqrt_n = int(math.sqrt(n))
    for p in small_primes:
        if p <= state.factored_to:
            # TODO start from higher primer already instead of iterating over smaller again
            continue

        if n % p == 0:
            state.add_prime_factor(p)
            return True
        if p > sqrt_n:
            state.add_prime_factor(n)
            return True

        state.factored_to = p

    return False
