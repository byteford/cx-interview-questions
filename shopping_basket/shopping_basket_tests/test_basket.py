import unittest
from shopping_basket import basket

class TestBasket(unittest.TestCase):
    bask = basket.basket()
    def test_allNone(self):
        sub,dis,total = self.bask.calc()
        self.assertEqual(sub,0)
        self.assertEqual(dis,0)
        self.assertEqual(total,0)
    def test_catNone(self):
        sub,dis,total = self.bask.calc(items = {"Baked Beans":4})
        self.assertEqual(sub,0)
        self.assertEqual(dis,0)
        self.assertEqual(total,0)
        pass
if __name__ == '__main__':
    unittest.main()
