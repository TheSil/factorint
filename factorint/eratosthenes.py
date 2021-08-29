from factorint.prime_list import PrimeList


def sieve_of_eratosthenes(to) -> PrimeList:
    primes = PrimeList()
    sieve = [True] * (to + 1)
    sieve[0] = sieve[1] = False
    i = 0
    for p in range(2, to // 2 + 1):
        if sieve[p]:
            i += 1
            primes.primes[i] = p
            kp = 2 * p
            while kp <= to:
                sieve[kp] = False
                kp += p

    for p in range(to // 2 + 1, to + 1):
        if sieve[p]:
            i += 1
            primes.primes[i] = p

    primes.b = to
    return primes
