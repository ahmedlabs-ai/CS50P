def main():
    amount_due = 50

    while amount_due > 0:
        print("Amount Due:", amount_due)
        coin = int(input("Insert coin: "))
        if coin == 25 or coin == 10 or coin == 5:
            amount_due = amount_due - coin

    print("Change Owed:", -amount_due )
main()