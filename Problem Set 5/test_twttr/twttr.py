vowels = ["a", "e", "i", "o", "u"]


def main():
    word = input("Input: ")
    print(shorten(word))


def shorten(word):
    result = ""

    for character in word:
        if character.lower() not in vowels:
            result = result + character

    return result


if __name__ == "__main__":
    main()