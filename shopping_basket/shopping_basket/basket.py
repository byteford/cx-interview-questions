class basket():
    _items = {}
    _catalog = {}
    _offers = {}
    #update stored catalog and/ or offers
    def update(self, catalog = None, offers = None):
        if catalog != None:
            self._catalog = catalog
        if offers != None:
            self._offers = offers
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
        #inits variables
        subTotal= discount= total = 0
        if catalog == None and not self._catalog:
            #is there a catalog passed or loaded
            print()
            print("==================================")
            print("========ERROR NEED CATALOG========")
            print("==================================")
            return subTotal, discount, total
        elif catalog != None:
            #updates the catalog if one has been passed
            self.update(catalog = catalog)
        if offers != None:
            self.update(offers = offers)
        if items == None and not self._items:
            #if no items have been passed return 0
            return subTotal, discount, total
        subTotal = self.calSubTotal(self._catalog,items)
        if subTotal < 0:
            return 0,0,0
        if self._offers:
            discount = self.calSingleOffers(self._catalog,self._offers,items)
        
        total = subTotal - discount
        return subTotal, round(discount,2), round(total,2)

    def calSubTotal(self,catalog, items):
        subTotal = 0
        for key, value in items.items():
            if catalog[key] < 0:
                print()
                print("==================================")
                print("=====PRICE CANNOT BE NEGITIVE=====")
                print("==================================")
                return 0
            if value < 0:
                print()
                print("==================================")
                print("=====AMOUNT CANNOT BE NEGITIVE====")
                print("==================================")
                return 0
            subTotal += catalog[key] * value
        return subTotal
    def calSingleOffers(self, catalog, offers, items):
        discount = 0
        for key, value in items.items():
            if key in offers:
                offer = offers[key]
                discount += offer.discount(amount=value,cost=catalog[key])
        return discount