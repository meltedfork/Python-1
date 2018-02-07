class Product(object):

    def __init__(self,price,item_name,weight,brand,status,tax,reason,condition):
        self.item_name=item_name
        self.price=price
        self.weight=weight
        self.brand=brand
        self.status=status
        self.tax=tax
        self.reason=reason
        self.condition=condition

    def sell(self):
        self.status="sold"
        return self

    def add_tax(self,tax):
        self.tax=tax
        print "Price of item is", self.price + self.tax
        return self.price + self.tax

    def returning(self,reason,condition):
        self.reason=reason
        self.condition=condition
        if self.condition=="defective":
            self.status="defective"
            self.price=0
        elif self.condition == "in the box, like new":
            self.status="for sale"
        elif self.condition=="open box":
            self.status="used"
            self.price= self.price*0.80
            return self

    def displayInfo(self):
        print "Name:", self.item_name
        print "Price:", self.price
        print "Weight:", self.weight
        print "Brand:", self.brand
        print "Status:", self.status
        print "Tax:", self.tax
        print "Reason for return: ", self.reason
        print "Condition:", self.condition
        return self

    
item1=Product("Cabinet",200,20,"Kyle's Cabinets","for sale",0.1,"Item is broken","defective")
item2=Product("Table",250,15,"Mable's Tables","for sale",0.1,"No longer needed","open box")
item3=Product("Chair", 175, 45, "Blair's Chairs","for sale",0.1,"duplicate purchase","in the box, like bew")


item1.displayInfo()
item2.displayInfo()
item3.displayInfo()

