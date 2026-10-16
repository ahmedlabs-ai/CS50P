import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    words = re.findall(r"\b\w+\b", s.lower())
    return words.count("um" )


if __name__ == "__main__":
    main()
