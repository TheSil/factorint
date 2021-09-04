import unittest

from factorint.small_primes import small_primes

class TestSmallPrimes(unittest.TestCase):
    def test_small_primes(self):
        last = small_primes[-1]
        sieve = [True]*(last+1)

        next = 0
        for p in range(2, last + 1):
            if sieve[p]:
                kp = 2*p
                while kp <= last:
                    sieve[kp] = False
                    kp += p

                self.assertEqual(p, small_primes[next])
                next += 1
        self.assertTrue(len(small_primes), next)


if __name__ == '__main__':
    unittest.main()
