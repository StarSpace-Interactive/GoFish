import random
Scard = ["A",1,2,3,4,5,6,7,8,9,10,"J","Q","K"]
Cplayer_hand = [] #player number = 2
Pplayer_hand = [] #player number = 1
def deal(player):
    '''deals out cards to the players'''
    if player == 1:
        for item in range(0,7):
            Pplayer_hand.append(random.choice(Scard))
    elif player == 2:
        for item in range(0,7):
            Cplayer_hand.append(random.choice(Scard))

#player makes a guess
    

#check players guess agianst computers hand if there is a match,-
#give the matching card from the computer to the player.- 
#if not have the player draw a card from the deck.do the same for the computer 
 
#check to see if there are 4 matching numbers in the players\computers hand
#increse the players\computer match counter by however many matches they made during that turn
#start the game loop
deal(1)
deal(2)
print(Cplayer_hand,Pplayer_hand )
