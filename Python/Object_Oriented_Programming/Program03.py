# Create class Cards with two list suits (Hearts, Diamonds, Clubs, Spades) and  values (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K)
# -> Create a class deck. That contains a method to get a card set containing 52 elements.
# -> Create class shuffle. That contains two methods to shuffle given cards and remove/pick a single card.
# -> Create two objects of the above class as players. Each player pick/remove 5 cards from the shuffle cards. Total points of both players and display name of winner player

import random

class cards:
    
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

class deck:

    def get_deck(self,list1,list2):
        deck_set = set()
        for suit in list1:
            for value in list2:
                deck_set.add(f'{suit}-{value}')
        return deck_set

class shuffle(deck):

    def shuffle_card(self):
        for _ in range(len(deck_of_card)):
            index = random.randint(0,len(deck_of_card)-1)
            element = deck_of_card.pop(index)
            deck_of_card.append(element)

    winner = []
    def pick_card(self):
        
        card_chosen = []
        for _ in range(5):
            card_picked = random.choice(deck_of_card)
            card_chosen.append(card_picked)
            deck_of_card.remove(card_picked)         
        
        taken_card = dict()
        total_points = 0
        for card in card_chosen:
            if card in points:
                taken_card[card] = points[card]
                total_points += points[card]
        print(taken_card)
        shuffle.winner.append(total_points)      

# player-1
obj = deck()
deck_of_card = list(obj.get_deck(cards.suits,cards.values)) # list of deck 52

# dict for points
arr = []
for number in range(1,53):
    arr.append(number)

points = dict(zip(deck_of_card,arr))

player1 = shuffle()
player1.shuffle_card()
player1.pick_card()

# player-2
obj = deck()
deck_card = obj.get_deck(cards.suits,cards.values) # list of deck 52

player2 = shuffle()
player1.shuffle_card()
player2.pick_card()

if max(shuffle.winner) == shuffle.winner[0]:
    print("Winner is Player-1 with {} points ".format(max(shuffle.winner)))
else:
    print("Winner is Player-2 with {} points ".format(max(shuffle.winner)))

# Done