class car(object):

    def __init__(self,name,price,speed,fuel,mileage,tax=0.12):
        self.name=name
        self.price=price
        self.speed=speed
        self.fuel=fuel
        self.mileage=mileage
        self.tax=tax
        if price > 10000:
            self.tax=0.15
            

    def displayAll (self):
        print self.name,self.price,self.speed,self.fuel,self.mileage,self.tax
        return self

Mustang=car("Mustang",25000,"250mph","Full","22mpg")
Nova=car("Nova",3000,"72mph","Half full","14mpg")
Accord=car("Accord",9775,"120mph","Full","34mpg")
Pinto=car("Pinto",120,"55mph","Empty","10mpg")
Ferrari=car("Ferrari",120000,"200mph","Full","4mpg")
Jeep=car("Jeep",9500,"110mph","Quarter full","24mpg")

Mustang.displayAll()
Nova.displayAll()
Accord.displayAll()
Pinto.displayAll()
Ferrari.displayAll()
Jeep.displayAll()

