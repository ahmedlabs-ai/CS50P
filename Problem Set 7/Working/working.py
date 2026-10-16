import re
import sys


def main():
    print(convert(input("Hours: ")))
    return(convert)

def convert(s):
    match = re.search(r"^([1-9]|1[0-2])(:([0-5][0-9]))? (AM|PM) to ([1-9]|1[0-2])(:([0-5][0-9]))? (AM|PM)$", s, re.IGNORECASE)

    if not match:
        raise ValueError

    hour1 = int(match.group(1))
    minute1 = int(match.group(3) or 0)
    period1 = match.group(4)
    hour2 = int(match.group(5))
    minute2 = int(match.group(7) or 0)
    period2 = match.group(8)

# hour validation
    if hour1 < 1 or hour1 > 12:
        raise ValueError

    if hour2 < 1 or hour2 > 12:
        raise ValueError
# minute validation

    if minute1 < 0 or minute1 > 59:
        raise ValueError

    if minute2 < 0 or minute2 > 59:
        raise ValueError

# timing range 1

    if period1 == "PM" and hour1 != 12:
        hour1 += 12
    elif period1 == "PM" and hour1 == 12:
        hour1 = 12
    elif period1 == "AM" and hour1 == 12:
        hour1 = 00
    elif minute1 == "":
        minute1 = 00

# timing range 2

    if period2 == "PM" and hour2 != 12:
        hour2 += 12
    elif period2 == "PM" and hour2 == 12:
        hour2 = 12
    elif period2 == "AM" and hour2 == 12:
        hour2 = 00
    elif minute2 == "":
        minute2 = 00

    if not (0 <= hour1 < 24) or not (0 <= hour2 < 24) or not (0 <= minute1 < 60) or not (0 <= minute2 < 60):
        raise ValueError

    final_time = f"{hour1:02}:{minute1:02} to {hour2:02}:{minute2:02}"
    return final_time


if __name__ == "__main__":
    main()
