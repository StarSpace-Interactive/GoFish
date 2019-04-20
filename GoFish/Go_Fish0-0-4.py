import random
from collections import Counter

pscore = 0#player score
cscore = 0#computers score

Scard = [1,2,3,4,5,6,7,8,9,10,11,12,13]#the cards

while True: #so the player can decide how many suites they want to play with.
    try:
        Suites = int(input("number of suites you want to play with: 2 or 4 "))
        if Suites == 2 or Suites == 4:
            deck = Suites * Scard#the card deck
            break
        else:
            print("invalid number")
    except ValueError:
        print("That is not a valid number , try agian...")

computer_hand = [] #player number = 2
player_hand = [] #player number = 1
pfished_card = []#player fished card

def deal(player,NumOfcards):
    
    '''deals out cards to the players,'''
    if player == 1:#deals to the player
        for item in range(0,NumOfcards):
            card = random.choice(deck)
            player_hand.append(card)
            deck.remove(card)
            
            if NumOfcards == 1:#tells the player what card they fished.
                while True:
                    if len(pfished_card) >= 1:
                        pfished_card.pop(0)
                    else:
                        pfished_card.append(card)
                        break
            
    elif player == 2:#deals to the computer
        for item in range(0,NumOfcards):
            Card = random.choice(deck)
            computer_hand.append(Card)
            deck.remove(Card)
            
def player_guess():#allows the player to guess a card.
    
    while True:
        print("your cards are: ",player_hand)
        print(f'you have this many matches: {pscore}')
        
        while True:#checks for inpoperly input values 
            try:
                result = int(input("what card would you like to guess? "))
                break
            except ValueError:
                print("that is not a valid number, try again...")
          
        if result in player_hand: # may not be needed for GUI version)
            if result in computer_hand:
                print("the computer gives this card ",result)
                computer_hand.remove(result)
                player_hand.append(result)
            else:
                print("the computer does not have this card , go fish ")
                deal(1,1)
                print(f'you fished: {pfished_card}')#prints out witch card the player has fished, see line 25
                break 
            
    else:
        print("I'm sorry you don't have that card ")

def Computer_guess():#allows the computer to guess a card.
    while True:
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
            break 

#game loop

deal(1,7)
deal(2,7)

Running = True
while Running:
    #-----checks to see who won----
    if len(player_hand) ==0:
        print("player wins!")
        break 
    elif len(computer_hand) ==0:
        print("computer wins!")
        
    print("")
    #print("this is the deck :", deck)
    #print("computers cards", computer_hand)
    player_guess()#allows the player to guess a card
    print('')
    Computer_guess()#allows the computer to guess a card
    
    #logic for checking if the players has a match     
    pcounts = Counter(player_hand)#logic for checking if the players has a match
    for num, count in pcounts.items():
        if Suites == 4:
            if count >= 4:
                player_hand = list(filter((num).__ne__, player_hand))
                pscore += 1
        else:
            if count >= 2:
                player_hand = list(filter((num).__ne__, player_hand))
                pscore += 1
    
    ccounts = Counter(computer_hand)#logic for checking if the computer has a match
    for num, count in ccounts.items():
        if Suites == 4:
            if count >= 4:
                computer_hand = list(filter((num).__ne__, computer_hand))
                cscore += 1
        else:
            if count >= 2:
                computer_hand = list(filter((num).__ne__, computer_hand))
                cscore += 1
    
    