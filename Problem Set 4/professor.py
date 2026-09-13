import random


def main():

    level = get_level()
    score = 0
    

    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        attempts = 0

        while True:
            print(x, "+", y, "=", end=" ")
            answer = int(input())

            if answer == (x + y):
                score += 1
                break
            else:
                print("EEE")
                attempts += 1

            if attempts == 3:
                print(x, "+", y, "=",x + y)
                break


def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            continue

        if level < 4 and level > 0:
            return level
        else:
            continue


def generate_integer(level):
    if level == 1:
        n = random.randint(0, 9)
    elif level == 2:
        n = random.randint(10, 99)
    elif level == 3:
        n = random.randint(100, 999)

    return n


if __name__ == "__main__":
    main()
