months = [
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
    date = input("Date: ")
    try:
        month,day,year = date.split("/")
        month = month.replace(" ","")
        year = year.replace(" ","")

        if(int(month) >= 1 and int(month) <= 12) and (int(day) >= 1 and int(day) <= 31):
            break
    except:
        try:
            old_month,old_day,year = date.split(" ")
            #old_month = old_month.replace(" ","")
            #old_year = old_year.replace(" ","")

            for i in  range(len(months)):
                if old_month == months[i]:
                    month = i + 1

            if not old_day.endswith(","):
                continue
            day = old_day.replace(",", "")
            if(int(month) >= 1 and int(month) <= 12) and (int(day) >= 1 and int(day)  <= 31):
                break
        except:
            print()
            pass
print(f"{year}-{int(month):02}-{int(day):02}")
