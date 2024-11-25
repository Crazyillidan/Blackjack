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
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 
              '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
    total = 0
    aces = 0
    for card in hand:
        rank = card.split()[0]
        total += values[rank]
        if rank == 'Ace':
            aces += 1

    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total


def display_hand():
    pass


def buy_chips():
    while True:
        try:
            amount = float(input("How many chips would you like to buy? "))
            if amount > 0:
                return round(amount, 2)
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def play_game():
    chips = db.read_chips()
    print(f"\nMoney: {chips}")

    while True:
        
        if chips < 5:
            print("\nYou don't have enough to place the minimum bet (5).")
            choice = input("Would you like to buy more? (y/n): ").lower()
            if choice == "y":
                chips += buy_chips()
                db.write_chips(chips)
                print(f"You now have {chips} chips.")
            else:
                print("Come back soon!")
                print("Bye!")
                break
    
def main():
    title()
    play_game()


if __name__ == "__main__":
    main()
