from cs50 import get_string


def main():
    # Prompt user for credit card number with validation
    while True:
        number = get_string("Number: ")
        if number.isnumeric() and len(number) <= 16:
            break

    # Conditions to verify if the cards are valid and, if so, from witch company

    # VISA -> Has to have 13 or 16 digits, the first digit must be 4
    if luhns(number) and (len(number) == 13 or len(number) == 16) and number[0] == '4':
        print("VISA")

    # American Express -> Has to have 15 digits, first two digits must be 34 or 37
    elif luhns(number) and len(number) == 15 and number[0] == '3' and (number[1] == '4' or number[1] == '7'):
        print("AMEX")

    # Master Card -> Has to have 16 digits, the first two digits must be 51, 52, 53, 54 or 55
    elif luhns(number) and len(number) == 16 and number[0] == '5' and (number[1] in ['1', '2', '3', '4', '5']):
        print("MASTERCARD")

    else:
        print("INVALID")


def luhns(num):
    doubles_sum = 0
    # Second-to-last digit and so on
    for i in range(len(num) - 2, -1, -2):
        # Multiplied by 2
        digit_double = int(num[i]) * 2

        # Checking if number > 9 to sum the digits
        if digit_double > 9:
            # Converts number to string
            s = str(digit_double)

            # Adds those numbers
            digit_double = int(s[0]) + int(s[1])

        doubles_sum += digit_double

    # Leftover digits sum + doubled sum
    lefts_sum = 0
    for i in range(len(num) - 1, -1, -2):
        lefts_sum += int(num[i])

    # Final Sum
    sum = doubles_sum + lefts_sum

    if (sum % 10 == 0):
        return True
    else:
        return False


main()
