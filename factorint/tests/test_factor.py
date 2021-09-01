import unittest

from factorint import factor
from factorint.state import FactorComponent


class TestFactor(unittest.TestCase):
    def test_factor_small(self):
        self.assertEqual([FactorComponent.prime_power(2, 1)],
                         factor.factor(2))

        self.assertEqual([FactorComponent.prime_power(2, 4)],
                         factor.factor(16))

        self.assertEqual([FactorComponent.prime_power(5, 1)],
                         factor.factor(5))

        self.assertEqual([FactorComponent.prime_power(2, 2),
                          FactorComponent.prime_power(5, 2)],
                         factor.factor(100))

    def test_factor_large(self):
        self.assertEqual([FactorComponent.prime_power(17, 1),
                          FactorComponent.prime_power(131, 1),
                          FactorComponent.prime_power(151, 1),
                          FactorComponent.prime_power(31755419, 1),
                          FactorComponent.prime_power(1155903747922039, 1)],
                         factor.factor(12343453453453453453453453457))

        self.assertEqual([FactorComponent.prime_power(31755419, 1),
                          FactorComponent.prime_power(1155903747922039, 1)],
                         factor.factor(36706207838934727779341))

        self.assertEqual([FactorComponent.prime_power(10000000000000000000000000000000000000121, 5)],
                         factor.factor(10000000000000000000000000000000000000121 ** 5))

    def test_factor_many_small_primes(self):
        P = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103,
             107, 109, 113]
        self.assertEqual([FactorComponent.prime_power(p, 1) for p in P],
                         factor.factor(31610054640417607788145206291543662493274686990))


if __name__ == '__main__':
    unittest.main()
