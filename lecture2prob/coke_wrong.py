#to learn from my mistake, pls refer to lecture2 loops coke.py homework

cost = int (50)
print ("Amount Due:",cost)
insert = int (input ("Insert Coin: "))
change = int (cost - insert)

while change > 0:
    print ("Amount Due:",change)
    while True:
        insert = int (input ("Insert Coin: "))
        if insert == int (25) or insert == int (10) or insert == int (5): #still wrong, 1st input never account for this
            break
        else:
            print ("Please try again, only accept 5, 10 or 25 cents")
            print ("Amount Due:",change)
            continue
    change -= insert

print ("Change Owed:", change) #how to account for when user overpay?, it will return -ve value
