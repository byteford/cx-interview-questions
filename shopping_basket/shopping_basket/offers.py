#To be implemented by other offers to add diffrent funcionality with each offer 
class offer():
    _multi = False
    #sets up the offer
    def __init__(self, **kwargs):
        pass
    #returns a float of the discount
    def discount(self,**kwargs):
        pass
    #returns if the offer is for multiple products or just one type
    def isMulti(self):
        return self._multi

#for offers where you get an amount for the pice of a diffrent amount, ie 3 for 2
class xfory(offer):
    _x = _y = 0
    def __init__(self, **kwargs):
        self._x = kwargs["x"]
        self._y = kwargs["y"]
        self._multi = False
    #kwargs are amount, cost
    def discount(self, **kwargs):
        amount = kwargs["amount"]
        cost = kwargs["cost"]
        dif = (self._x-self._y)
        saving = amount / self._x
        return round(int(saving) *(cost*dif),2)

class percent(offer):
    _percent = 0
    def __init__(self, **kwargs):
        self._percent = kwargs["percent"]
        self._multi = False
    def discount(self, **kwargs):
        amount = kwargs["amount"]
        cost = kwargs["cost"]
        saving = cost * (self._percent /100)
        return round(saving*amount,2)