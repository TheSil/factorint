import unittest

from factorint import miller_rabin


class TestMillerRabin(unittest.TestCase):
    def test_miller_rabin(self):
        self.assertEqual(False, miller_rabin.is_composite_miller_rabin(2, 2))
        self.assertEqual(False, miller_rabin.is_composite_miller_rabin(3, 2))
        self.assertEqual(False, miller_rabin.is_composite_miller_rabin(17, 2))
        self.assertEqual(False, miller_rabin.is_composite_miller_rabin(221, 174))
        self.assertEqual(True, miller_rabin.is_composite_miller_rabin(221, 137))
        self.assertEqual(True, miller_rabin.is_composite_miller_rabin(252601, 85132))
        self.assertEqual(False, miller_rabin.is_composite_miller_rabin(104717, 96152))
        self.assertEqual(False, miller_rabin.is_composite_miller_rabin(577757, 314997))
        self.assertEqual(True, miller_rabin.is_composite_miller_rabin(95721889, 21906436))


if __name__ == '__main__':
    unittest.main()
