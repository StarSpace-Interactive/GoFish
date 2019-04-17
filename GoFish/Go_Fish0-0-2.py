import random

Scard = [1,2,3,4,5,6,7,8,9,10,11,12,13]
Suites = 4
deck = Suites * Scard

Cplayer_hand = [] #player number = 2
Pplayer_hand = [] #player number = 1



def deal(player,NumOfcards):
    
    '''deals out cards to the players'''
    if player == 1:
        for item in range(0,NumOfcards):
            card=random.choice(deck)
            Pplayer_hand.append(card)
            deck.remove(card)
    elif player == 2:
        for item in range(0,NumOfcards):
            Card = random.choice(deck)
            Cplayer_hand.append(Card)
            deck.remove(Card)
            
def player_guess():
    print("your cards are: ",Pplayer_hand)
    result = int(input("what card would you like to guess? "))
    if result in Pplayer_hand: # may not be needed for GUI version)
        if result in Cplayer_hand:
            print("the computer gives this card ",result)
            Cplayer_hand.remove(result)
            Pplayer_hand.append(result)
        else:
            print("the computer does not have this card , go fish ")
            deal(1,1)
            
    else:
        print("I'm sorry you don't have that card ")

def Computer_guess():
    result = random.choice(Cplayer_hand)
    print("the computer guesses:", result)
    if result in Pplayer_hand:
        print("you give this card: ", result)
        Pplayer_hand.remove(result)
        Cplayer_hand.append(result)
    else:
        print("the computer fishes")
        deal(1,1)

#check to see if there are 4 matching numbers in the players\computers hand
#increse the players\computer match counter by however many matches they made during that turn
#game loop

deal(1,7)
deal(2,7)

Running = True
while Running:
    print("")
    print("this is the deck :", deck)
    print(len(deck))
    print(" ")
    print("computers cards", Cplayer_hand)
    player_guess()
    print(" ")
    print("the computers turn.")
    Computer_guess()
