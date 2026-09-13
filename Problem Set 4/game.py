import random

while True:
    try:
        level =int(input("Level: "))
    except ValueError:
        continue
        if level > 0 :
            break
        else:
            continue
    number = random.randint(1,level)
    while True:
        guess = int(input("Guess: "))
        if guess <= 0 :
            continue

        if guess == number:
            print("Just right!")
            break
        elif guess > number:
            print("Too large!")
        elif guess < number:
            print("Too small!")