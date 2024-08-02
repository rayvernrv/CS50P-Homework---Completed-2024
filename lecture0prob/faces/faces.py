#Replace :) with 🙂 and :( with 🙁
def convert (faces):
    faces=faces.replace(":)","🙂")
    faces=faces.replace(":(","🙁")
    return faces

#Prompt user to type and ends with :) or :(.
def main ():
    sentence=input ("Say something and end with :) or :( Thanks! ")
    new=convert(sentence)
    print (new)

main()


#Alternate solution just for testing purpose
"""
testing=input ("Test - Say something and end with :) or :( Thanks! ").replace(":)","🙂").replace(":(","🙁")
print (testing)
"""
