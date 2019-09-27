import unittest
from shopping_basket import utility

class testUtility(unittest.TestCase):
    def test_basketSort(self):
        cat = {"Baked Beans": 0.99,"Biscuits": 1.20, "Sardines": 1.89, "Shampoo (Small)": 2.00, "Shampoo (Medium)": 2.50, "Shampoo (Large)": 3.50}
        self.assertEqual(utility.sortItems(cat,utility.DicToList({"Shampoo (Small)":1, "Shampoo (Medium)":2,"Shampoo (Large)":3})),["Shampoo (Large)","Shampoo (Large)","Shampoo (Large)","Shampoo (Medium)","Shampoo (Medium)","Shampoo (Small)"])
    def test_DictToList(self):
        self.assertEqual(utility.DicToList({"Shampoo (Small)":1, "Shampoo (Medium)":2,"Shampoo (Large)":3}),["Shampoo (Small)","Shampoo (Medium)","Shampoo (Medium)","Shampoo (Large)","Shampoo (Large)","Shampoo (Large)"])
if __name__== "__main__":
    unittest.main()