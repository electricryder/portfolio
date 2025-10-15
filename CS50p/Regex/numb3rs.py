import re


def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    try:
        if matches := re.search(r"^(\w\w?\w?)\.(\w\w?\w?)\.(\w\w?\w?)\.(\w\w?\w?)$", ip):
            block1 = int(matches.group(1))
            block2 = int(matches.group(2))
            block3 = int(matches.group(3))
            block4 = int(matches.group(4))
        else:
            return False
    except ValueError:
        return False

    else:
        if (
            0 <= block1 <= 255
            and 0 <= block2 <= 255
            and 0 <= block3 <= 255
            and 0 <= block4 <= 255
        ):
            return True
        else:
            return False


if __name__ == "__main__":
    main()

