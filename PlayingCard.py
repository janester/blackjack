#Jane Sternbach
from random import *

class PlayingCard: #create class

    def __init__(self,rank,suit):
        #make instance variables
        self.rank=rank 
        self.suit=suit

        #adjust variables for cards
        if self.rank==1 or self.rank==14:
            self.rank="Ace"
        elif self.rank==11:
            self.rank="Jack"
        elif self.rank==12:
            self.rank="Queen"
        elif self.rank==13:
            self.rank="King"

        if self.suit=="c":
            self.suit="Clubs"
        elif self.suit=="d":
            self.suit="Diamonds"
        elif self.suit=="h":
            self.suit="Hearts"
        else:
            self.suit="Spades"

    def getRank(self): #accessor method
        return self.rank


    def getSuit(self): #accessor method
        return self.suit


    def BJValue(self):
        #adjust cards to Blackjack values
        if self.rank=="Jack" or self.rank=="Queen" or self.rank=="King":
            return self.rank==10

        if self.rank==14:
            return self.rank==1

    def __str__(self): #print the card name correctly
        self.cardName=str(self.rank)+" of "+str(self.suit)
        return self.cardName



##def main():
##    n=eval(input("please input a number: "))
##    r=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
##    s=["d","c","s","h"]
##    for i in range(n):
##        rank=r[randrange(0,14)]
##        suit=s[randrange(0,4)]
##        c=PlayingCard(rank,suit)
##        print(c)
##
##main()
