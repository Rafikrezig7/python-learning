import art
print(art.logo)
print("Welcome to the secret auction program.\n")

bids={}

bidding_over=False
#the name
while not bidding_over:
    print("What's your name?")
    while True:
        name=input(">>> ")
        if name=="":
            print("Please enter a name.")
        elif bids.get(name):
            print(f"There is already a bid by {name}. Please enter a different name.")
        else:
            break
#the amount
    while True:
        bid_str=input(">>> $")
        if bid_str == "0":
            print("$0 is not a proper bid. Please try again.")
        elif not bid_str.isdigit():
            print("Please enter a valid bid. Only numbers are allowed.")
        else:
            bid=int(bid_str)
            break
    bids[name]=bid
#other bidders
    print("Are there any other bidders? (yes/no)")
    choice=input(">>> ").lower()
    if choice=="no":
        bidding_over=True
    print("\n"*100)
#find highest bid
winner_name=""
top_bid=0
for key in bids:
    if bids[key]>top_bid:
        top_bid=bids[key]
        winner_name=key
print(f"The winner is {winner_name} with a bid of ${top_bid}")