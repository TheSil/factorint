import queue
from enum import Enum

class FactorType(Enum):
    Unknown = 1
    Prime = 2
    Composite = 3

class FactorComponent:
    def __init__(self, base, exp, type=FactorType.Unknown):
        self.base = base
        self.exp = exp
        self.type = type

    def to_int(self):
        return self.base ** self.exp

    def __repr__(self):
        base = repr(self.base)
        if self.type == FactorType.Composite:
            base = f"COMP({base})"
        elif self.type == FactorType.Unknown:
            base = f"UNK({base})"
        return f"{base}^{self.exp}" if self.exp > 1 else f"{base}"


def max_factor_component(p, n) -> FactorComponent:
    e = 0
    pe = p
    while n % pe == 0:
        e += 1
        pe *= p
    return FactorComponent(p, e)


class FactorizationState:
    def __init__(self, n):
        self.prime_comps = []
        self.unfactored = []
        self.to_factor_comps: queue.Queue = queue.Queue()
        self.to_factor_comps.put(FactorComponent(n, 1))
        self.to_factor = None
        self.n = n
        self.primes_checked_up_to = 1

    def add_prime_factor(self, p):
        to_factor = self.to_factor

        if to_factor.base == p:
            # original component was prime in fact
            self.prime_comps.append(to_factor)
            to_factor.type = FactorType.Prime
            self.to_factor = FactorComponent(1, 1)
            return

        comp = max_factor_component(p, to_factor.base)
        self.to_factor.base //= comp.to_int()
        comp.exp *= to_factor.exp
        comp.type = FactorType.Prime
        self.prime_comps.append(comp)

    def add_divisor(self, d):
        to_factor = self.to_factor

        comp = max_factor_component(d, to_factor.base)
        self.to_factor.base //= comp.to_int()
        comp.exp *= to_factor.exp
        self.to_factor_comps.put(comp)
