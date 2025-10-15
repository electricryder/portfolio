while True:
    fuel_level = input("Fraction > ").split("/")
    try:
        X = int(fuel_level[0])
        Y = int(fuel_level[1])
        frac = int(round((X / Y) * 100 , 0))
        if frac > 100:
            continue
    except (ValueError, ZeroDivisionError):
        pass
    else:
        if frac >= 99:
            print("F")
        elif frac <= 1:
            print("E")
        else:
            print(f"{frac}%")
        break
