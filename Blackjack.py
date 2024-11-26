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


def display_hand(hand, hide_first_card=False):
    if hide_first_card:
        print(hand[1])
    else:
        for card in hand:
            print(card)


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
            
        while True:
            try:
                bet = float(input(f"Bet amount: "))
                if 5 <= bet <= min(1000, chips):
                    bet = round(bet, 2)
                    break
                else:
                    print(f"Invalid bet. You must be bet between 5 and 1000.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        chips -= bet
        db.write_chips(chips)



        deck = create_deck()
        dealer_hand = [deck.pop(), deck.pop()]
        player_hand = [deck.pop(), deck.pop()]

        print("\nDEALER'S SHOW CARD:")
        display_hand(dealer_hand, hide_first_card=True)
        print("\nYOUR CARDS:")
        display_hand(player_hand)

        player_total = calculate_hand_value(player_hand)

        while True:
            if player_total > 21:
                print("\nYOUR POINTS: ", player_total)
                print("\nSorry. You lose.")
                break

            print("\nHit or stand? (hit/stand): ", end="")
            choice = input().lower()

            if choice ==  "hit":
                player_hand.append(deck.pop())
                print("\nYOUR CARDS:")
                display_hand(player_hand)
                player_total = calculate_hand_value(player_hand)
            elif choice == "stand":
                break
            else:
                print("Invalid choice, please choose 'hit' or 'stand'.")
                
        if player_total <= 21:
            print("\nDEALER'S CARDS:")
            dealer_total = calculate_hand_value(dealer_hand)
            while dealer_total < 17:
                dealer_hand.append(deck.pop())
                dealer_total = calculate_hand_value(dealer_hand)
            display_hand(dealer_hand)
            print("\nYOUR POINTS:", player_total)
            print("DEALER'S POINTS:", dealer_total)

            if dealer_total > 21 or player_total > dealer_total:
                print("\nCongratulations! You win!")
                chips += bet * 2  
            elif player_total < dealer_total:
                print("\nSorry. You lose.")
            else:
                print("\nIt's a tie!")
                chips += bet

        db.write_chips(chips)
        print(f"Money: {chips}")
        play_again = input("\nPlay again? (y/n): ").lower()
        if play_again != "y":
            print("\nCome back soon!")
            print("Bye!")
            break
    
def main():
    title()
    play_game()


if __name__ == "__main__":
    main()
