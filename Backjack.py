#Jane Sternbach
#4/16/12
#This program will simulate a game of blackjack

#import necessary modules
from Deck import *
from PlayingCard import *
from random import *
from button2 import *
from graphics import *


class Blackjack: #create new class

    def __init__(self,dHand=[],pHand=[]):
        self.dHand=dHand
        self.pHand=pHand
        self.deck=Deck() #create new deck
        self.deck.shuffle() #shuffle deck

    def makeCard(self,card,xpos,ypos): #additonal method that pairs the card dealt with the picture of that card
        card=card
        card=card.split()
        rank=card[0]
        suit=card[2]

        if suit=="Spades":
            suit="s"
        elif suit=="Hearts":
            suit="h"
        elif suit=="Clubs":
            suit="c"
        else:
            suit="d"

        if rank=="Jack":
            rank="11"
        if rank=="Queen":
            rank="12"
        if rank=="King":
            rank=13
        if rank=="Ace":
            rank=1
        rank=str(rank)

        self.cardPic=Image(Point(xpos,ypos),suit+rank+".gif")
        return self.cardPic #returns the picture of the card in the correct spot 
        

    def initDeal(self,gwin,xposD,yposD,xposP,yposP):
        #Start with the player's hand first
        card1p=self.deck.dealCard()
        self.pHand.append(card1p)
        card1p=self.makeCard(card1p,xposP,yposP)
        card1p.draw(gwin)
        
        card2p=self.deck.dealCard()
        self.pHand.append(card2p)
        card2p=self.makeCard(card2p,xposP+100,yposP)
        card2p.draw(gwin)

        #Now the dealer's hand
        card1d=self.deck.dealCard()
        self.dHand.append(card1d)
        card1d=self.makeCard(card1d,xposD+100,yposD)
        card1d.draw(gwin)

        card2d=self.deck.dealCard()
        self.dHand.append(card2d)
        self.hiddenCard=self.makeCard(card2d,xposD,yposD)
        #one card needs to be face down, but counted
        card2d=Image(Point(xposD,yposD),"b2fv.gif")
        card2d.draw(gwin)
        


    def hit(self,gwin,xpos,ypos,hand):
        newCard=self.deck.dealCard() #deal a new card
        hand.append(newCard) #add it to the list
        newCard=self.makeCard(newCard,xpos,ypos)
        newCard.draw(gwin)

    
        
    def evaluateHand(self,hand):
        handTotal=0 #accumulator to know which person got higher total
        j=0
        for i in hand:#go through the hand list one by one
            c=hand[j]
            j=j+1
            c=c.split()
            #give appropriate cards the correct values
            if c[0]=="Jack" or c[0]=="Queen" or c[0]=="King":
                c[0]=10
                value=c[0]
            elif c[0]=="Ace" and handTotal+11<21:
                c[0]=11
                value=c[0]
            elif c[0]=="Ace" and handTotal+11>21:
                c[0]=1
                value=c[0]
            else:
                value=eval(c[0])
            handTotal=handTotal+value #accumulate values
            self.handTotal=handTotal
        return self.handTotal #return hand total

    def dealerPlays(self,gwin,xpos,ypos):
        self.evaluateHand(self.dHand) #call this method to have a total returned to you
        while self.handTotal<17: #while the total is less than 17, keep hitting
            self.hit(gwin,xpos,ypos,self.dHand)
            xpos=xpos+100
            self.handTotal=self.evaluateHand(self.dHand) #update hand total
        self.hiddenCard.draw(gwin) #ahow the hidden card
            

def main():
    win=GraphWin("Blackjack",800,800) #make GUI

    #introduce the program
    intro=Text(Point(400,400),"This program will simulate a game of Blackjack.\n Click anywhere to continue.")
    intro.draw(win)
    
    win.getMouse()
    
    intro.undraw()
    
    game=Blackjack()

    #show which hand is which
    title1=Text(Point(200,100),"Dealer")
    title1.draw(win)
    titel2=Text(Point(200,500),"You")
    titel2.draw(win)

    #make all the buttons
    deal=Button(win,Point(600,100),50,50,"Deal")
    hitBt=Button(win,Point(300,400),50,50,"Hit")
    stayBt=Button(win,Point(400,400),50,50,"Stay")
    Quit=Button(win,Point(500,400),50,50,"Quit")
    
    deal.activate()
    pt=win.getMouse()

    #activate all the other buttons only after the cards are dealt
    while deal.clicked(pt)==False:
        hitBt.deactivate()
        stayBt.deactivate()
        Quit.deactivate()
        pt=win.getMouse()

    #deal cards
    firstDeal=game.initDeal(win,100,200,100,600)

    #activate buttons
    hitBt.activate()
    stayBt.activate()
    Quit.activate()
    xpos=300 #accumulator variable so that the cards aren't on top of one another

    #play while quit isn't clicked
    while Quit.clicked(pt)==False:
        pt=win.getMouse()
        if hitBt.clicked(pt)==True: #allow the player to hit until they bust
            hit=game.hit(win,xpos,600,game.pHand)
            xpos=xpos+100
            pHand=game.evaluateHand(game.pHand)
            if pHand>21:
                bust=Text(Point(400,500),"Sorry, you busted. The Dealer wins.")
                bust.draw(win)
        elif stayBt.clicked(pt)==True: #if they chose to stay, let the dealer go
            dealerGo=game.dealerPlays(win,300,200)
            pHand=game.evaluateHand(game.pHand)
            dHand=game.evaluateHand(game.dHand)
            print("dhand: ",dHand)
            print("phand: ",pHand)
            #share results of who won the game
            if pHand>dHand:
                pWin=Text(Point(400,500),"You win!")
                pWin.draw(win)
            elif dHand==pHand:
                dWin=Text(Point(400,500),"You Lose")
                dWin.draw(win)
            elif pHand<dHand<=21:
                dWin=Text(Point(400,500),"You Lose")
                dWin.draw(win)
            else:
                pWin=Text(Point(400,500),"You win!")
                pWin.draw(win)
        else:
            pt=win.getMouse()

    win.close() #close when button is clicked

main()
    
    

            
