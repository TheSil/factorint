class PrimeList:
    def __init__(self):
        self.primes = {}
        self.a = 0
        self.b = 0

    def is_prime(self, n):
        return n in self.primes.values()

    def prime(self, n):
        return self.primes[n]

    def __iter__(self):
        for p in self.primes.values():
            yield p
