import random
import db

def title():
    print("BLACKJACK!")
    print("BlackJack payout is 3:2")
        
    
def create_deck():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    deck = [rank + " of " + suit for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck

def calculate_hand_value(hand):
    pass


def display_hand():
    pass


def buy_chips():
    pass


def play_game():
    pass


def main():
    title()



if __name__ == "__main__":
    main()
