## Documentation

To just run the code please use the unittests in the "shopping_basket_tests" folder

some tests give False negitives if all the tests are ran at the same time

There is 3 files of tests "test_basket" tests the overall functionaly of the project, "test_offers" tests the logic of each offer and "test_utility" that tests 2 utility functions I made 

Please see below for infomation on how to run the functions provided. 

basket 

Update(catalog = None, offers = None)

		catalog : Dict[string, float] (name, cost)
		
		offers 	: Dict[string, offer] (name, list[offer object])
		
	updates the catalog and offers doesnt do anything if they values are None
	
clearBasket()

	clears the stored basket
	
addItem(name,amount=1)

		name	: string
		
		amount	: int
		
	adds an item to the basket
	
addItems(items)

		items 	: Dict[string,int] (name, amount)
		
	loops though a Dictionay of items and runs adItem on them
	
calc(catalog=None,offers=None,items=None)

		catalog : Dict[string, float] (name, cost)
		
		offers 	: Dict[string, offer] (name, list[offer object])
		
		items 	: Dict[string,int] (name, amount)
		
	returns subtotal, discount, total : float
	
	proccess the subtotal, amount of discount to apply and a total
	
calcSubTotal(catalog, items)

		catalog : Dict[string, float] (name, cost)
		
		items 	: Dict[string,int] (name, amount)
		
	returns subtotal: float
	
	calculates a subtotal from a catalog and list of items
	
calcSingleOffers(catalog,offers,items)

		catalog : Dict[string, float] (name, cost)
		
		offers 	: Dict[string, offer] (name, list[offer object])
		
		items 	: Dict[string,int] (name, amount)
		
	returns discount: float
	
	Calculates how much discount to give based only on sigle product offers	
	
calcMultiOffers(catalog,offers,items)

		catalog : Dict[string, float] (name, cost)
		
		offers 	: Dict[string, offer] (name, list[offer object])
		
		items 	: Dict[string,int] (name, amount)
		
	returns discount: float
	
	Calculates how much discount to give based only on multi product offers	
	
	
offers

__init__(**kwargs)

	Does not do anything on its own
	
discount(**kwargs)

	Does not do anything on its own
	
ifMulti()

	returns a bool based on whether the offer is for a single product or effects the whole basket

xfory(offer)

__init__(**kwargs)

		kwargs = (x:int,y:int) 
		
		x being the amount needed for the discount and the y being the amout the customor pays for.
		
		ie. 3 for 2 , x would be 3 and y would be 2
		
discount(**kwargs)

		kwargs = (amount:int,cost:float) 
		
		amount is the amount being bought
		
		cost is cost per item
		
		returns a float
		
percent(offer)

__init__(**kwargs)

		kwarfgs = percent:int
		
		percent is a whole number > 0
		
discount(**kwargs)

		kwargs = (amount:int,cost:float) 
		
		amount is the amount being bought
		
		cost is cost per item
		
		returns a float
		
buyxGetCheap(offer):

__init__(**kwargs)

		kwarfgs = amount:int
		
		amount if how many to get one free
		
discount(**kwargs)

		kwargs = (catalog:Dict[string, float] (name, cost),items:Dict[string,int] (name, amount)) 
		
		returns a float
		
		works out whats the most amount of money the could be saved
		
An example of a basic calc function:

cat = {"Baked Beans": 0.99,"Biscuits": 1.20}

Bask = basket.basket()

sub,dis,total = bask.calc(catalog=cat,offer={"Baked Beans":offers.xfory(x=3,y=2)}, items = {"Baked Beans":4, "Biscuits":1})
