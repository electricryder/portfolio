import sys
names = []

while True:
    try:
        names.append(input("Name> ").strip())

    except EOFError:
        break

print("Adieu, adieu, to ", end= "")

for i in range(len(names)):
    if i == 0:
        print(names[0], end= "")

    elif i == len(names) - 1 and len(names) == 2:
        print(f" and {names[i]}", end= "")

    elif i == len(names) - 1:
        print(f", and {names[i]}", end= "")

    else:
        print(f", {names[i]}", end= "")
print()
