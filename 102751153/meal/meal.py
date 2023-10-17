def main():
    ask = input("What time is it? ")
    time = convert(ask)
    if time >= 7 and time <= 8:
        print("breakfast time")
    elif time >= 12 and time <= 13:
        print("lunch time")
    elif time >=18 and time <= 19:
        print("dinner time")


def convert(time):
    hours , minutes = time.split(":")
    mint = float(minutes) / 60
    hrs = float(hours)
    return hrs + mint


if __name__ == "__main__":
    main()