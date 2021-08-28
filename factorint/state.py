import queue


class FactorComponent:
    def __init__(self, base, exp):
        self.base = base
        self.exp = exp

    def to_int(self):
        return self.base ** self.exp

    def __repr__(self):
        return f"{self.base}^{self.exp}" if self.exp > 1 else f"{self.base}"


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
        self.factored_to = 1

    def add_prime_factor(self, p):
        to_factor = self.to_factor

        if to_factor.base == p:
            # original component was prime in fact
            self.prime_comps.append(to_factor)
            self.to_factor = FactorComponent(1, 1)
            return

        comp = max_factor_component(p, to_factor.base)
        self.to_factor.base //= comp.to_int()
        comp.exp *= to_factor.exp
        self.prime_comps.append(comp)

    def add_divisor(self, d):
        to_factor = self.to_factor

        comp = max_factor_component(d, to_factor.base)
        self.to_factor.base //= comp.to_int()
        comp.exp *= to_factor.exp
        self.to_factor_comps.put(comp)
        if self.to_factor.base != 1:
            self.to_factor_comps.put(self.to_factor)
        self.to_factor = FactorComponent(1, 1)
