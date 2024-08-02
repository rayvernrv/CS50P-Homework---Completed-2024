#Alternative, more specific into the function you want, and make your code succint
#from random import choice

#toys = random.choice (["Bubu","Yier", "Labong", "Avoca"])
#print (toys)

import random #import every functions etc. in random module
import statistics

toys = random.choice (["Bubu","Yier","Labong","Avoca"])
print (toys)

print ("--------------------------------------------------")

number = random.randint(1,10) #include 1 to 10
print (number)

print ("--------------------------------------------------")

cards = ["Jack","Queen","King","Ace"]
random.shuffle(cards)
for card in cards:
    print (card)

print ("--------------------------------------------------")
score = statistics.mean([100,90])
print (score)
