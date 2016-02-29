#Jane Sternbach

from PlayingCard import *
from random import *

class Deck: #create class
    def __init__(self):
        self.deck=[] #start a new deck
        for s in ["c","d","h","s"]: #populate deck in order
            for r in range(1,14):
                c=PlayingCard(r,s)
                c=str(c)
                self.deck.append(c)
                
    def shuffle(self): #shuffle deck but replacing cards randomly
        for n in range(52):
            i=randrange(0,52)
            j=randrange(0,52)
            holder=self.deck[i]
            self.deck[i]=self.deck[j]
            self.deck[j]=holder
        return self.deck
            
    def dealCard(self): #deals a card and removes it from the deck
        card=self.deck.pop(0)
        return card

    def cardsLeft(self): #tells how many cards are left
        j=0
        for i in self.deck:
            j=j+1
        return j

           
