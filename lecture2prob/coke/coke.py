#Make the cost of a coke remains at 50 cents throughout
cost = int (50)
amount_paid = int (0) #I learned that I can define an amount beforehand, to use later
accepted_coins = [5,10,25] #can put a condition in a list

#Using while loop when unsure how many iteration needed
while amount_paid < cost:
    #Calculate and print the amount due based on accumulative amount_paid
    print ("Amount Due:", cost - amount_paid)
    insert = int (input ("Insert Coin: "))
    #If statement below is to check for accepted denomination using list defined above
    #Instead of using if insert == 25 or insert == 10...
    if insert in accepted_coins:
        #The amount paid will become 10, 20 so on
        #and (cost - amount_paid) will be cumulative amount paid at each iteration
        amount_paid +=insert
    else:
        print ("Please try again, only accept 5, 10 or 25 cents")

#Break out of here when amount paid > cost
#If user overpaid, change owed will show positive value
change = amount_paid - cost
print ("Change Owed:", change)
