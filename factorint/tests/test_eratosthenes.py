import unittest

from factorint import eratosthenes


class TestEratosthenes(unittest.TestCase):
    def test_small_sieve(self):
        self.assertEqual({}, eratosthenes.sieve_of_eratosthenes(1).primes)
        self.assertEqual({1: 2}, eratosthenes.sieve_of_eratosthenes(2).primes)
        self.assertEqual({1: 2,
                          2: 3,
                          3: 5,
                          4: 7},
                         eratosthenes.sieve_of_eratosthenes(10).primes)
        up_to_500 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
                     101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197,
                     199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313,
                     317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439,
                     443, 449, 457, 461, 463, 467, 479, 487, 491, 499]
        self.assertEqual({i+1: p for i, p in enumerate(up_to_500)},
                      eratosthenes.sieve_of_eratosthenes(500).primes)


if __name__ == '__main__':
    unittest.main()
