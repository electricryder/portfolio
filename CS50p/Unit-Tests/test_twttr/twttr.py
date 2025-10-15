def main():
    word = input("Input > ")
    print(f"Output > {shorten(word)}")


def shorten(word):
    for char in word:
        if char in "aeiou":
            word = word.replace(char, "")
    return word


if __name__ == "__main__":
    main()
