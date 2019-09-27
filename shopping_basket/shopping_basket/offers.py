#To be implemented by other offers to add diffrent funcionality with each offer 
class offer():
    #sets up the offer
    def setup(self, multi = False, **kwargs):
        pass
    #returns a float of the discount
    def discount(self,**kwargs):
        pass
    #returns if the offer is for multiple products or just one type
    def isMulti(self):
        pass