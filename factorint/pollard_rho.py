import math

from .state import FactorizationState


def find_by_pollard_rho(state: FactorizationState) -> bool:
    n = state.to_factor.base

    def g(x):
        return (x * x + 1) % n

    max_pollard_iters = 100

    x, y, d = 2, 2, 1
    i = 0
    while d == 1 and i < max_pollard_iters:
        z = 1
        for j in range(100):
            x = g(x)
            y = g(g(y))
            z *= abs(x - y)
            z %= n
        d = math.gcd(z, n)
        i += 1

    if d == n or d == 1:
        return False

    state.add_divisor(d)
    return True
