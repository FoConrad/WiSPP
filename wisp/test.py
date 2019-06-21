import unittest

class TestExprs(unittest.TestCase):
    def test_add_prec(self):
        print('test')
        self.assertEqual(2+3 * 5, 25)


# This will be fun to get working
if __name__ == '__main__':
    unittest.main()
