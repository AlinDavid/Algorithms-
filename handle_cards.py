'''
In many card games each player is dealt a specific number of cards after the deck
has been shuffled. Write a function, deal, which takes the number of hands, the
number of cards per hand, and a deck of cards as its three parameters. Your function
should return a list containing all of the hands that were dealt. Each hand will be
represented as a list of cards.
When dealing the hands, your function should modify the deck of cards passed
to it as a parameter, removing each card from the deck as it is added to a player’s
hand. When cards are dealt, it is customary to give each player a card before any
player receives an additional card. Your function should follow this custom when
constructing the hands for the players
Display all of the hands of cards, along with the cards remaining in the deck after
the hands have been dealt
'''


from random import *


def create_deck():

    number = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "A", "J", "Q", "K"]
    suit = ["s", "h", "d", "c"]

    return [i + j for i in number for j in suit]

def shuffle(cards):

    for i in range(0, len(cards)):

        other_position = randrange(0, len(cards))
        cards[i], cards[other_position] = cards[other_position], cards[i]

def main():

    cards = create_deck()
    
    print("The original deck is:")
    print(cards)
    print()

    shuffle(cards)
    
    print("The shuffled deck is:")
    print(cards)
    print()

if __name__ == '__main__':
    main()
