month_list = [
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

def main():
    while True:
        date = input("Date > ").strip()
        if "/" in date:
            date_model_1 = date.split("/")
            if len(date_model_1) != 3:
                continue
            try:
                month = int(date_model_1[0])
                day = int(date_model_1[1])
                year = int(date_model_1[2])
            except ValueError:
                continue

            if month < 1 or month > 12 or day < 1 or day > 31 or year < 0:
                continue

            print(f"{year:4}-{month:2}-{day:2}".replace(" ", "0"))
            break
        else:
            date_model_2 = date.split(" ")
            if len(date_model_2) != 3 or "," not in date_model_2[1]:
                continue

            try:
                month = month_list.index(date_model_2[0]) + 1
                day = int(date_model_2[1].replace(",", ""))
                year = int(date_model_2[2])
            except ValueError:
                continue

            if month < 1 or month > 12 or day < 1 or day > 31 or year < 0:
                continue

            print(f"{year:4}-{month:2}-{day:2}".replace(" ", "0"))
            break


main()
