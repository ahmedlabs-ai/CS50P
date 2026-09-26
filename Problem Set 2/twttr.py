vowels = ["a", "e", "i", "o", "u"]
text = input("Input: ")
for character in text:
    if character.lower() not in vowels:
        print(character, end="")
print()