players = {
    "Bubu" :"Brown",
    "Yier" : "White",
    "Labong" : "Orange",
    "Avoca" : "Green",
}

new_list = "\n".join(f"{value} {key}" for key,value in players.items()) #will only work with .items as it will help retrieve key-value
print (new_list)

print ("-------------------------------------")
new_list = "-".join(f"{value} {key}" for key,value in players.items()) #will only work with .items as it will help retrieve key-value
print (new_list)

print ("-------------------------------------")
for player in players: #for every key in dict
    print (player, players[player]) #print each [key,value]
