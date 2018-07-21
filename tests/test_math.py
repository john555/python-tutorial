import unittest

class TestMath(unittest.TestCase):
  def test_add(self):
    self.assertEqual(2, 1 + 1)
  
  def test_division(self):
    with self.assertRaises(ZeroDivisionError):
      2 / 0

# if __name__ == "__main__":
#   unittest.main()

# python3 -m unittest
