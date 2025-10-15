def main():
    hour = convert(input("What time is it?\n> "))

    if 7 <= hour <= 8:
        print("breakfast time")
    elif 12 <= hour <= 13:
        print("lunch time")
    elif 18 <= hour <= 19:
        print("dinner time")


def convert(time):
    #Hour part if hour format is ##:## p.m.
    if "p.m." in time:
        time = time.replace("p.m.", "")
        hour = int(time.split(":")[0]) + 12
    elif "a.m." in time:
        time = time.replace("a.m.", "")
        #Hour part if hour is ##:## a.m.
        hour = int(time.split(":")[0])
    else:
        #Hour part if hour is 24h
        hour = int(time.split(":")[0])

    #Minute part converted to decimal
    minute = int(time.split(":")[1]) / 60
    #Sum and conversion to a float value
    float_time = float(hour + minute)

    return float_time


if __name__ == "__main__":
    main()
