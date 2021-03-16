# A Ridiculously Simple Bidding System

import random
import sys

# Fancy function to generate random people
def genRanBidders(blist, n):
    blist.clear()
    maxPrice = int(seller[0] * (random.random() + 1) * 1.5) # Random generates a decimal between 0.0 to 1.0 # Change 1.5 to control randomness
    for i in range(n):
        price = random.randint(seller[0], maxPrice)
        quantity = random.randint(1, seller[1])
        name = random.choice(list(open('first_names.txt'))).strip()
        blist.append([price, quantity, name])

# Sorting function
def getBid(bidder):
    return bidder[0] * bidder[1]

# Print the list for debug
def printList(list):
    for x in range(len(list)):
        print(list[x])


# Seller set-price (minimum) and available quantity
seller = [14, 100]

# Bidders with their bidding price and quantity + name
bidders = [
    [3, 60, "Naushi"],
    [5, 90, "Imashi"]
]

genRanBidders(bidders, 50)

# Sort of the bidders
bidders.sort(reverse=True, key=getBid)

printList(bidders)

#sys.exit() <-- For debugging

availQuantity = seller[1]
curr = 0 # Current bidder we are looking at
selBidders = [] # Selected bidders
while (availQuantity and curr < len(bidders)): # Stop when we hit 0
    # Check if the quantity the bidder asked for is available
    # If not ask the bidder if it is okay to buy it
    # Else just give the bidder the amount, automatically
    if (availQuantity >= bidders[curr][1]):
        print("%s is the %d bidder, he is automatically getting %d quantity" % (bidders[curr][2], curr+1, bidders[curr][1]))
        availQuantity = availQuantity - bidders[curr][1]
        selBidders.append([curr+1, bidders[curr][2], bidders[curr][1]])
    else:
        print("%s is the %d bidder, he has asked for %d quantity, but available quantity is %d, proceed? (y/n)" % (bidders[curr][2], curr+1, bidders[curr][1], availQuantity))
        resp = input()
        if (resp == "y"):
            selBidders.append([curr+1, bidders[curr][2], availQuantity])
            availQuantity = 0
            print("Bidder \"%s\" chose to buy the remaining quantity" % bidders[curr][2])
            # Bidder got all the remaining quantity
            # Inform other bidders they lost the bid
    curr = curr + 1
    print("Currently available quantity is %d" % availQuantity)

if (availQuantity == 0):
    print("\nEverything has been sold!\n")
else: print("\n %d has been left out!\n" % availQuantity)

print("Rank | Name | Quantity Bought")
printList(selBidders)