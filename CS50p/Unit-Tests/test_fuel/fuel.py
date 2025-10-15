def main():
    fuel_level = input("Fraction > ")
    print(percentage(convert(fuel_level)))



def convert(fraction):
    fuel_level = fraction.split("/")
    X = int(fuel_level[0])
    Y = int(fuel_level[1])
    frac = int(round((X / Y) * 100 , 0))
    if frac > 100:
        raise ValueError("X value is greater than Y!")
    if Y == 0:
        raise ZeroDivisionError("Can't divide by Zero!")
    return str(frac)


def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}"


if __name__ == "__main__":
    main()
