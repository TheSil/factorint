import math

from factorint.state import FactorizationState


# wheel division - trial division while avoiding multiples of few smallest primes
class WheelFactorization:

    def __init__(self, base=(2, 3, 5)):
        self.base = base
        self.prod = 1
        for p in base:
            self.prod *= p

        # sieve the initial offsets
        offsets_sieve = (self.prod + 1) * [True]
        for p in base:
            kp = p
            while kp <= self.prod:
                offsets_sieve[kp] = False
                kp += p

        self.offsets = []
        for d in range(1, self.prod + 1):
            if offsets_sieve[d]:
                self.offsets.append(d)


wheel = WheelFactorization()


def find_by_wheel_division(state: FactorizationState) -> bool:
    start = state.factored_to + 1
    trial_division_limit = 1000000

    #  k*prod  >= wheel_from => k >= wheel_from/prod
    k = (start + 1) // wheel.prod
    kprod = k * wheel.prod
    n = state.to_factor.base
    sqrt_n = int(math.sqrt(n))
    while kprod <= min(trial_division_limit, sqrt_n):
        for off in wheel.offsets:
            d = kprod + off
            if n % d == 0:
                state.add_prime_factor(d)
                return True
        kprod += wheel.prod

    if kprod > sqrt_n:
        state.add_prime_factor(n)
        return True

    return False
