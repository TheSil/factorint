from factorint.lucas_pseudoprime import is_lucas_pseudoprime
from factorint.miller_rabin import is_composite_miller_rabin
from factorint.state import FactorizationState, FactorType
from factorint.utils import is_perfect_square, jacobi


def is_probable_prime_baillie_psw(n):
    if is_perfect_square(n):
        return False

    if is_composite_miller_rabin(n, 2):
        return False

    D = 5
    sign = 1
    while jacobi(sign * D, n) != -1:
        D += 2
        sign = -sign
    D = sign * D

    if is_lucas_pseudoprime(n, D):
        return True

    return False


def check_prime_baillie_psw(state: FactorizationState) -> bool:
    n = state.to_factor.base
    if is_probable_prime_baillie_psw(n):
        state.add_prime_factor(n)
        return True

    state.to_factor.type = FactorType.Composite
    return False
