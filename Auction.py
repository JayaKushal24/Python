import os

book={}#empty dictionary
os.system('cls')#for clearing the terminal
print("Welcome to the Auction Program")

def highest_bidder():#checking the highest value in the dictionary
    highest_bid=0
    for bidder in book:
        if book[bidder]>highest_bid:
            highest_bid=book[bidder]
    print(f"\n\nThe highest bid is '{highest_bid}Rs'  by '{bidder}' ")

more_data=True
while more_data:#loop runs until more_bids is no
    name=input("what is your name?\n")
    bid=int(input("what\'s your bid?\n Rs "))
    more_bids=input("Are there any other bidders? Type Yes or NO\n").lower()
    os.system('cls')
    book[name]=bid
    if more_bids =="no":
        more_data=False
highest_bidder()#calliing function


