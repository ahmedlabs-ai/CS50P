def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False

    if not s[0].isalpha() or not s[1].isalpha():
            return False

    number_started = False

    for character in s:
            if not character.isalpha() and not character.isdigit():
                return False

            if character.isdigit():

                 if not number_started and character == "0":
                    return False
                 number_started = True

            if number_started and not character.isdigit():
                return False

    return True


main()
