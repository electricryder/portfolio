import sys
import random


def main():
    level = get_level()
    score = 0

    for _ in range(0, 10):
        errors = 0
        x = int(generate_integer(level))
        y = int(generate_integer(level))
        cpu_result = x + y

        while True:
            if errors == 3:
                print(f"{x} + {y} = {cpu_result}")
                break
            try:
                guess_result = int(input(f"{x} + {y} = "))

                if guess_result == cpu_result:
                    score += 1
                    break
                else:
                    print("EEE")
                    errors += 1
                    continue

            except ValueError:
                print("EEE")
                errors += 1
                continue

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))

            if 1 <= level <= 3:
                return level
            else:
                continue
        except ValueError:
            continue
        except KeyboardInterrupt:
            print()
            sys.exit()


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    if level == 2:
        return random.randint(10, 99)
    if level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("Invalid value!")


if __name__ == "__main__":
    main()
