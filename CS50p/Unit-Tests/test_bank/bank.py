def main():
    greeting = input("Greeting > ")
    print(f"${value(greeting)}")


def value(greeting):
    first_word = greeting.split()[0]
    first_letter = greeting.lower()[0]

    if "hello" in first_word:
        return 0
    elif first_letter == "w":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
