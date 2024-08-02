import random

def main():
    levels = get_level()
    correct = 0  # this is cumulative, so shouldnt include in the loop
    for _ in range(10):
        numbers = generate_integer(levels)
        tries = 0  # number of attemps - this will reset for each question, so must be in the loop
        while tries < 3:
            try:
                answer = int(input(f"{numbers[0]} + {numbers[1]} = "))
                sum = numbers[0] + numbers[1]
                if answer == sum:
                    correct += 1  # need to count correct answer.
                    break
                else:
                    raise ValueError  # must raise ValueError. In case user input alphabet, "sum" has value associated
            except ValueError:
                print("EEE")
                tries += 1
                if tries == 3:
                    print(f"{numbers[0]} + {numbers[1]} = {sum}")
                    break
                pass
        continue
    print("Score:", correct)

# get_level from user
def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level <= 0 or level > 3:
                raise ValueError
            elif 1 <= level <= 3:
                break
        except ValueError:
            pass
    return level  # must return level

# generate integer based on level (n digits)
def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        return x, y  # return a tuple
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
        return x, y
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
        return x, y


if __name__ == "__main__":
    main()
