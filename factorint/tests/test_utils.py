import unittest

from factorint import utils


class TestUtils(unittest.TestCase):
    def test_isqrt(self):
        for b in range(1, 100):
            for k in range(b * b, (b + 1) * (b + 1)):
                self.assertEqual(b, utils.isqrt(k))

    def test_iroot(self):
        for b in range(2, 6):
            for e in range(2, 6):
                for k in range(b ** e, (b + 1) ** e):
                    self.assertEqual(b, utils.iroot(k, e))

    def test_ilog2(self):
        for b in range(1, 15):
            for k in range(2 ** b, 2 ** (b + 1)):
                self.assertEqual(b, utils.ilog2(k))

    def test_jacobi(self):
        self.assertEqual(-1, utils.jacobi(1001, 9907))
        self.assertEqual(1, utils.jacobi(19, 45))


if __name__ == '__main__':
    unittest.main()
