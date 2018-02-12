class  bike(object):

    def __init__(self,price, max_speed,miles = 0):
        self.price = price
        self.max_speed = max_speed 
        self.miles = miles

    def displayInfo(self):
        print self.price,self.max_speed,self.miles
        return self

    def ride(self):
        print "Riding..."
        self.miles+=10
        print "Total miles on bike is",self.miles
        return self

    def reverse(self):
        if self.miles < 5:
            print "Cannot reverse below zero, you moron."
            return self
        print "Reversing..."
        self.miles-=5
        print "Total miles on bike is",self.miles
        return self

Blue = bike(450,"25mph")
Red = bike(300, "15mph")
Yellow = bike(375, "22mph")

Blue.ride().ride().ride().reverse().displayInfo()
Red.ride().ride().reverse().reverse().displayInfo()
Yellow.reverse().reverse().reverse().displayInfo()

