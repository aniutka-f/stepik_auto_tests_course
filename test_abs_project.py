# def test_abs1():
#       assert abs(-42) == 42, "Should be absolute value of a number"

# if __name__ == "__main__":
#       test_abs1()
#       print("All tests passed!")

import unittest


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        self.assertEqual(abs(-42), 42, "Should be absolute value of a number")

    def test_abs2(self):
        self.assertEqual(abs(-42), -42, "Should be absolute value of a number")


if __name__ == "__main__":
    unittest.main()

