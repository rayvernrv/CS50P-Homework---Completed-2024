import random

while True:
    try:
        level = int(input("Level: "))
        if level <= 0:
            pass
        elif level > 0:
            n = random.randint(1, level)
            break
    except ValueError:
        pass

while True:
    try:
        output = int(input("Guess: "))
        if output == n:
            break
        elif output > n:
            print("Too large!")
            pass
        elif output < n:
            print("Too small!")
            pass
    except ValueError:
        pass

print("Just right!")
