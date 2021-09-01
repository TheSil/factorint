import unittest

from factorint import lucas_pseudoprime


class TestLucas(unittest.TestCase):
    def test_known_pseudoprimes(self):
        self.assertEqual(True, lucas_pseudoprime.is_lucas_pseudoprime(5459, -7))
        self.assertEqual(True, lucas_pseudoprime.is_lucas_pseudoprime(5777, 5))
        self.assertEqual(True, lucas_pseudoprime.is_lucas_pseudoprime(10877, 5))
        self.assertEqual(True, lucas_pseudoprime.is_lucas_pseudoprime(16109, 13))
        self.assertEqual(True, lucas_pseudoprime.is_lucas_pseudoprime(18971, -11))
        self.assertEqual(True, lucas_pseudoprime.is_lucas_pseudoprime(22499, -15))

    def test_non_pseudoprimes(self):
        self.assertEqual(False, lucas_pseudoprime.is_lucas_pseudoprime(63, -7))
        self.assertEqual(False, lucas_pseudoprime.is_lucas_pseudoprime(123, 5))
        self.assertEqual(False, lucas_pseudoprime.is_lucas_pseudoprime(4123, 5))
        self.assertEqual(False, lucas_pseudoprime.is_lucas_pseudoprime(79137, 13))
        self.assertEqual(False, lucas_pseudoprime.is_lucas_pseudoprime(17391, -11))
        self.assertEqual(False, lucas_pseudoprime.is_lucas_pseudoprime(14329, -15))


if __name__ == '__main__':
    unittest.main()
