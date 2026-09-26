while True:
    try:
        per = input("Fraction: ")
        x,y = per.split("/")
        x = int(x)
        y = int(y)
        answer = round(x/y *100)
        if x > y or x < 0 or y < 0:
             continue

        elif answer <= 1:
            print("E")
            break
        elif answer >= 99:
            print("F")
            break
        else:
            print(answer,"%",sep="")
            break
    except(ValueError, ZeroDivisionError):
                continue