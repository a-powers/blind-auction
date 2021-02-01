from replit import clear
from art import logo

print(logo)
bid_dict = {}
bidding_finished = False

while not bidding_finished:
    names = input("What is your name?")
    prices = int(input("What do you bid? $")
    bid_dict[names] = prices
    should_continue = input("Are there more bidders? Type 'y' or 'n'.")
    if should_continue == 'n'
    bidding_finished = True
    elif should_continue == 'y':
        clear()
