import random
from collections import Counter

pscore = 0#player score
cscore = 0#computers score

Scard = [1,2,3,4,5,6,7,8,9,10,11,12,13]#the cards
Suites = 4
deck = Suites * Scard#the card deck


computer_hand = [] #player number = 2
player_hand = [] #player number = 1



def deal(player,NumOfcards):
    
    '''deals out cards to the players,'''
    if player == 1:
        for item in range(0,NumOfcards):
            card=random.choice(deck)
            player_hand.append(card)
            deck.remove(card)
            
    elif player == 2:
        for item in range(0,NumOfcards):
            Card = random.choice(deck)
            computer_hand.append(Card)
            deck.remove(Card)
            
def player_guess():
    print("your cards are: ",player_hand)
    print(f'you have this many matches: {pscore}')
    result = int(input("what card would you like to guess? "))
    if result in player_hand: # may not be needed for GUI version)
        if result in computer_hand:
            print("the computer gives this card ",result)
            computer_hand.remove(result)
            player_hand.append(result)
        else:
            print("the computer does not have this card , go fish ")
            deal(1,1)
            
    else:
        print("I'm sorry you don't have that card ")

def Computer_guess():
    result = random.choice(computer_hand)
    print("the computer guesses:", result)
    print(f'the computer has this many matches: {cscore}')
    if result in player_hand:
        print("you give this card: ", result)
        player_hand.remove(result)
        computer_hand.append(result)
    else:
        print("the computer fishes")
        deal(2,1)


#game loop

deal(1,7)
deal(2,7)

Running = True
while Running:
    print("")
    print("this is the deck :", deck)
    print("computers cards", computer_hand)
    player_guess()#allows the player to guess a card
    print()
    Computer_guess()#allows the computer to guess a card
    
    pcounts = Counter(player_hand)#logic for checking if the players has a match
    for num, count in pcounts.items():
        if count >= 4:
            player_hand = list(filter((num).__ne__, player_hand))
            pscore += 1
    
    ccounts = Counter(computer_hand)#logic for checking if the computer has a match
    for num, count in ccounts.items():
        if count >= 4:
            computer_hand = list(filter((num).__ne__, computer_hand))
            cscore += 1
    
            
