from replit import clear
from art import logo

print(logo)
bid_dict = {}
bidding_finished = False

while not bidding_finished():
    name = input("What is your name?\n").lower()
    bid = int(input("What is your bid?\n$ "))
    bid_dict[name] = bid


more_bidders = input("Are there more bidders? Type 'Y' or 'N'.\n").lower


