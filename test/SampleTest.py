import unittest
from Sample import fact


class TestFactorial(unittest.TestCase):
    """
    Our basic test class
    """

    def test_fact1(self):
        """
        The actual test.
        Any method which starts with ``test_`` will considered as a test case.
        """
        res = fact(0)
        self.assertEqual(res, 1)

    def test_fac2(self):
        """
         The actual test.
         Any method which starts with ``test_`` will considered as a test case.
        """
        res = fact(5)
        self.assertEqual(res, 120)


if __name__ == '__main__':
    unittest.main()