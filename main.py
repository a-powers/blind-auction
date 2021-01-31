from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)

bid_dict = {}
bidding_finished = False

def final_bidder(bid_record = bid_dict):
    highest_bid = 0
    winner = ""
    for bids in bid_record:
        bid_lookup = bid_record[bids]
        if bid_lookup > highest_bid:
            highest_bid = bid_lookup
            winner = bids
    print(f"The winner is {winner} with a bid amount of ${highest_bid}.")




while not bidding_finished:
    name = input("What is your name?\n").lower()
    bid = int(input("What is your bid?\n$ "))
    bid_dict[name] = bid
    more_bidders = input("Are there more bidders? Type 'Y' or 'N'.\n").lower
    if more_bidders == "N":
        bidding_finished = True
        final_bidder(bid_dict)
    elif more_bidders == "Y":
        clear()