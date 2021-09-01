from factorint.eratosthenes import sieve_of_eratosthenes
from factorint.state import FactorizationState
from factorint.utils import isqrt

small_primes = sieve_of_eratosthenes(10000)


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
            state.add_prime_factor(n)
            return True

    return start_n != n
