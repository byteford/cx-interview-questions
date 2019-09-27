class basket():
    _items = {}
    _catalog = {}
    _offers = {}
    #update stored catalog and/ or offers
    def update(self, catalog = None, offers = None):
        pass
    #clear any stored items in the basket
    def clearBasket(self):
        pass
    #add an item of any quantity
    def addItem(self, name, amount = 1):
        pass
    #add a Dict of items to the existing basket
    def addItems(self, items):
        pass
    # calculates the value, returns:
    # SubTotal, Discount, Total
    # can also replace any stored values (DOES NOT ADD TO)
    def calc(self, catalog=None, offers=None, items = None):
        if items == None and not self._items:
            return 0, 0, 0
        if(catalog == None and not self._catalog):
            print()
            print("==================================")
            print("========ERROR NEED CATALOG========")
            print("==================================")
            return 0,0,0
        pass