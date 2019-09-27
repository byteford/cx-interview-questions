import unittest
from shopping_basket import basket

class TestBasket(unittest.TestCase):
    def test_allNone(self):
        bask = basket.basket()
        self.assertEqual(bask.calc(),0)
if __name__ == '__main__':
    unittest.main()
