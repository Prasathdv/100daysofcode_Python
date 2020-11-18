# This module is Silent auction module which uses dictionaries and nesting concepts.
from replit import clear
from art import logo

#  Display the Auction logo
print(logo)

# Initialization
bid_data = {}
bid_completed = False

# Find max bid amount


def find_max_bidder(bidder):
    max_amount = 0
    max_bidder = ''
    for bid in bidder:
        bid_amount = bidder[bid]
        if bid_amount > max_amount:
            max_amount = bid_amount
            max_bidder = bid
    print(f"The winner is {max_bidder} and bid amount is {max_amount}")


while not bid_completed:
    name = input("Enter Bidder`s name: ")
    price = int(input("Enter bid price here: Rs."))
    # Write it in the bid_data dictionary
    bid_data[name] = price
    game_continue = input("Are there any other bidders? Type 'yes' or 'no' \n")

    if game_continue == "no":
        bid_completed = True
        clear()
        find_max_bidder(bid_data)
    elif game_continue == "yes":
        clear()
