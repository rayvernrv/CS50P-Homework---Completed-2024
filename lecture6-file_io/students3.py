#csv #dictwriter
import csv

name = input("Name: ")
home = input("Home: ")

with open("students3.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name,home]) #write specifically in a list

print ("---------------------------")
#Use dict to associate keys with values in case column got swapped
with open("students3.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name","home"]) #fieldnames to set the column names in csv
    writer.writerow({"name": name, "home": home})
