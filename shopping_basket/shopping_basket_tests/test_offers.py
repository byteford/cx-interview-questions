import unittest
from shopping_basket import offers

class TestOffers(unittest.TestCase):
    def test_xfory(self):
        xfory = offers.xfory(x=3,y=2)
        self.assertEqual(xfory.discount(amount=3,cost=0.99),0.99)
        self.assertEqual(xfory.discount(amount=2,cost=0.99),0)
        self.assertEqual(xfory.discount(amount=10,cost=0.99),2.97)
        xfory2 = offers.xfory(x=10,y=5)
        self.assertEqual(xfory2.discount(amount=30,cost=0.99),14.85)
        self.assertEqual(xfory2.discount(amount=20,cost=0.99),9.9)
        self.assertEqual(xfory2.discount(amount=100,cost=0.99),49.5)
    def test_percent(self):
        per = offers.percent(percent=25)
        self.assertEqual(per.discount(amount=2,cost=1.89), .94)
    def test_xgetCheap(self):
        cheap = offers.buyxGetCheap(amount=3)
        cat = {"Shampoo (Large)": 3.50}
        self.assertEqual(cheap.discount(catalog=cat,items={"Shampoo (Large)":3}),3.50)
    def test_xgetCheapmulti(self):
        cheap = offers.buyxGetCheap(amount=3)
        cat = {"Shampoo (Small)": 2.00, "Shampoo (Medium)": 2.50, "Shampoo (Large)": 3.50}
        self.assertEqual(cheap.discount(catalog=cat,items={"Shampoo (Large)":3, "Shampoo (Medium)":2,"Shampoo (Small)":1}),5.50)
    def test_xgetCheapmultirev(self):
        cheap = offers.buyxGetCheap(amount=3)
        cat = {"Shampoo (Small)": 2.00, "Shampoo (Medium)": 2.50, "Shampoo (Large)": 3.50}
        self.assertEqual(cheap.discount(catalog=cat,items={"Shampoo (Small)":1, "Shampoo (Medium)":2,"Shampoo (Large)":3}),5.50)
if __name__ == '__main__':
    unittest.main()