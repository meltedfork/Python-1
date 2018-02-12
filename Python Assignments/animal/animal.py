class animal(object):
    def __init__(self,name="",health=100):
        self.name=name
        self.health=health

    def walk(self):
        self.health-=1
        return self

    def run(self):
        self.health-=5
        return self

    def display_health(self):
        print self.health, "health left"
        return self

class dog(animal):
    def __init__(self,health=150):
        super(dog,self).__init__()
        self.health=health

    def pet(self):
        self.health+=5
        return self 

class dragon(animal):
    def __init__(self,health=170):
        super(dragon,self).__init__()
        self.health=health
    
    def fly(self):
        self.health-=10
        return self

    def display_health(self):
        super(dragon,self).display_health()
        print "I am a dragon!"
        return self
        


animal1=animal()
animal2=dog()
animal3=dragon()



animal1.walk().walk().walk().run().run().display_health()
animal2.walk().walk().walk().run().run().pet().display_health()
animal3.run().run().run().fly().display_health()    
