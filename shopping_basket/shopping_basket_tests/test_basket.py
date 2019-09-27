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
        bask= basket.basket()
        sub,dis,total = bask.calc(items = {"Baked Beans":4})
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
        sub,dis,total = self._bask.calc(catalog = self._cat,offers={"Baked Beans":[offers.xfory(x=3,y=2)]}, items = {"Baked Beans":4})
        self.assertEqual(sub,3.96)
        self.assertEqual(dis,0.99)
        self.assertEqual(total,2.97)
    def test_percentDiscount(self):
        sub,dis,total = self._bask.calc(catalog = self._cat,offers={"Sardines":[offers.percent(percent=25)]}, items = {"Sardines":2})
        self.assertEqual(sub,3.78)
        self.assertEqual(dis,0.94)
        self.assertEqual(total,2.84)
    def test_negPrice(self):
        sub,dis,total = self._bask.calc(catalog = {"Baked Beans": -1}, items = {"Baked Beans":4})
        self.assertEqual(sub,0)
        self.assertEqual(dis,0)
        self.assertEqual(total,0)
    def test_negAmount(self):
        sub,dis,total = self._bask.calc(catalog = self._cat, items = {"Baked Beans":-4})
        self.assertEqual(sub,0)
        self.assertEqual(dis,0)
        self.assertEqual(total,0)
    def test_notInCat(self):
        sub,dis,total = self._bask.calc(catalog = self._cat, items = {"Baked":4})
        self.assertEqual(sub,0)
        self.assertEqual(dis,0)
        self.assertEqual(total,0)
    def test_addItemBeforeCalc(self):
        bask= basket.basket()
        bask.addItem("Baked Beans",4)
        sub,dis,total = bask.calc(catalog = self._cat)
        self.assertEqual(sub,3.96)
        self.assertEqual(dis,0)
        self.assertEqual(total,3.96)
    def test_addItemsBeforeCalc(self):
        bask= basket.basket()
        bask.addItems({"Baked Beans":4,"Sardines":1})
        sub,dis,total = bask.calc(catalog = self._cat)
        self.assertEqual(sub,5.85)
        self.assertEqual(dis,0)
        self.assertEqual(total,5.85)
    def test_clearBasket(self):
        bask= basket.basket()
        bask.addItems({"Baked Beans":4,"Sardines":1})
        bask.clearBasket()
        sub,dis,total = bask.calc(catalog = self._cat)
        self.assertEqual(sub,0)
        self.assertEqual(dis,0)
        self.assertEqual(total,0)
    def test_xcheapDiscount(self):
        sub,dis,total = self._bask.calc(catalog = self._cat,offers={"multi":offers.buyxGetCheap(amount=3)},items={"Shampoo (Small)":1, "Shampoo (Medium)":2,"Shampoo (Large)":3})
        self.assertEqual(sub,17)
        self.assertEqual(dis,5.5)
        self.assertEqual(total,11.5)
if __name__ == '__main__':
    unittest.main()
