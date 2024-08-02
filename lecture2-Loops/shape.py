print ("3 by 3 square")
#print a 3 by 3 square
for i in range (3): #print number of rows
    for j in range (3): #print number of # in a row
        print ("#", end="")
    print ()
print ("Triangle - Ver.1")
#print a triangle (Ver.1)
height = 3
i=1
for row in range (height):
    for column in range (i,i+1): #if specify (2,3), it will print 1 row only
        print ("#"*i)
        i += 1
print ("Triangle - Ver.2")
#print a triangle (Ver.2)
j = 1
for _ in range (j,j+3):
    print ("#"*j)
    j +=1

print ("Triangle - Wrong version")
#Wrong solution
k = 1
for row in range (3):
    for column in range (k): #if never specify a range, if j = 2, it will count from print 1st and 2nd row
        print ("#"*k) #each row print 2
    k += 1
