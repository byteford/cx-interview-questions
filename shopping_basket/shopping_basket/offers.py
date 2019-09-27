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
    def discount(self, **kwargs):
        pass