from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)
name = input("What is your name?\n").lower()
bid = int(input("What is your bid?\n$ "))
more_bidders = input("Are there more bidders? Type 'Y' or 'N'.\n").lower

bid_dict = {}

def all_bids(new_name, new_bids):
    bid_dict[name] = bid

if more_bidders == "y":
    



all_bids(name, bid)
print(bid_dict)