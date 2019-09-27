import unittest
from shopping_basket import basket
from shopping_basket import offers
class TestBasket(unittest.TestCase):
    _bask = basket.basket()
    _cat = {"Baked Beans": 0.99,"Biscuits": 1.20, "Sardines": 1.89, "Shampoo (Small)": 2.00, "Shampoo (Medium)": 2.50, "Shampoo (Large)": 3.50}
    def test_allNone(self):
        sub,dis,total = self._bask.calc()
        self.assertEqual(sub,0)
        self.assertEqual(dis,0)
        self.assertEqual(total,0)
    def test_catNone(self):
        _bask= basket.basket()
        sub,dis,total = _bask.calc(items = {"Baked Beans":4})
        self.assertEqual(sub,0)
        self.assertEqual(dis,0)
        self.assertEqual(total,0)
        pass
    def test_1itemNoOffer(self):
        sub,dis,total = self._bask.calc(catalog = self._cat, items = {"Baked Beans":4})
        self.assertEqual(sub,3.96)
        self.assertEqual(dis,0)
        self.assertEqual(total,3.96)
    def test_itemsNoOffer(self):
        sub,dis,total = self._bask.calc(catalog = self._cat, items = {"Baked Beans":4, "Biscuits": 1})
        self.assertEqual(sub,5.16)
        self.assertEqual(dis,0)
        self.assertEqual(total,5.16)
    def test_xforyDiscount(self):
        sub,dis,total = self._bask.calc(catalog = self._cat,offers={"Baked Beans":offers.xfory(x=3,y=2)}, items = {"Baked Beans":4})
        self.assertEqual(sub,3.96)
        self.assertEqual(dis,0.99)
        self.assertEqual(total,2.97)
if __name__ == '__main__':
    unittest.main()
