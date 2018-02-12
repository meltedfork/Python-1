import random

class Deck(object):
  def __init__ (self):
    self.amount = 52
    self.cards=[]
    suits = ["Hearts","Diamonds","Clubs","Spades"]
    for value in range (1,14):
      for suit in suits:
        newCard=Card(value,suit)
        self.cards.append(newCard)
        
  def deal (self):
      self.cards[random.randint(1,52)]
      return self.cards[random.randint(1,52)]
      
class Card (object):
  def __init__ (self,value,suit):
    self.suit=suit
    self.value=value
    
    
# newCard=Card(5,"Diamonds")
bicycle=Deck()

card=bicycle.deal()

print card.suit
print card.value