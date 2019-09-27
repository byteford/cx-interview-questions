import unittest
from shopping_basket import offers

class TestOffers(unittest.TestCase):
    def test_xfory(self):
        xfory = offers.xfory(x=3,y=2)
        self.assertEqual(xfory.discount(amount=3,cost=0.99),0.99)
        self.assertEqual(xfory.discount(amount=2,cost=0.99),0)
        self.assertEqual(xfory.discount(amount=10,cost=0.99),2.97)

if __name__ == '__main__':
    unittest.main()