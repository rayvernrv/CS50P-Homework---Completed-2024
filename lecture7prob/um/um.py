import re


def main():
    print(count(input("Text: ")))


def count(s):
    return int((len(re.findall(r"\bum\b", s, re.IGNORECASE))))


if __name__ == "__main__":
    main()
