import emoji #pip install emoji

user_input = input("Input: ")
print("Output:", emoji.emojize(user_input, language="alias"))
