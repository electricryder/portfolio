groceries = {}

def main():
    while True:
        try:
            fruit = input().upper()
        except EOFError:
            break
        if fruit in groceries.keys():
            number = groceries[fruit] + 1
        else:
            number = 1
        groceries.update({fruit : number})

    for _ in sorted(groceries.keys()):
        print(groceries[_], _)


main()
