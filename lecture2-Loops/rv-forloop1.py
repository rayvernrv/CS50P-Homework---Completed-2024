s = "hello"
i = 0
for i in range(1,len(s)):  # Start from 1 to avoid index error
    print(s[i-1], s[i], sep=",")  # Prints pairs of consecutive characters

print ("------------------------------------------------")

t = "hello"
j = 1
for _ in range(1,len(s)):
    print(t[j-1], t[j], sep=",")
    j += 1
print ("------------------------------------------------")

if t[2:] == "llo":
    print ("bubu")

u = "fiver"
for _ in u[2:]: #this one only helps to count how many character after char[2](inclusive), so left v,e,r -> 3 character
    print (u) #so will print (u) 3 times
    
print ("------------------------------------------------")
for _ in range (2,5): #same as above
    print (u)
