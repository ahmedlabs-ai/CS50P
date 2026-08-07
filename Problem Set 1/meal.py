def main():
    time = input("What time is it? ")
    meal_time = convert(time)
    if 7 <= meal_time <= 8:
        print("breakfast time")
    elif 12 <= meal_time <= 13:
        print("lunch time")
    elif 18 <= meal_time <= 19:
        print("dinner time")


def convert(time):
    hour, minute = time.split(":")
    hour = int(hour)
    minute = int(minute)
    return hour + minute / 60

if __name__ == "__main__":
    main()
