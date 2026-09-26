months =[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    try:
        date = input("Date: ").capitalize()

        if "/" in date :
            
            month, day, year = date.split("/")
            if 1 <= int(month) <= 12 and 1 <= int(day) <= 31:
                month = int(month)
                day = int(day)
                year = int(year)
                print(f"{year}-{month:02d}-{day:02d}")
                break
        elif "," in date:
            month_day, year = date.split(",")
            month, day = month_day.split(" ") 
            if 1 <= int(day) <= 31:
                day = int(day)
                year = int(year)
                month = months.index(month)+1 
                print(f"{year}-{month:02d}-{day:02d}") 
                break 
    except ValueError:
        continue 