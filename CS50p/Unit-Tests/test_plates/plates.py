def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if is_twoletters(s) and validlenght(s) and num_position(s) and is_alphanumerical(s):
        return True
    else:
        return False


def is_twoletters(s):
    if len(s) < 2:
        return False
    return True if s[0].isalpha() or s[1].isalpha() else False


def validlenght(s):
    return True if len(s) <= 4 and len(s) >= 2 else False


def num_position(s):
    #First, we'll verify if the Plate has numbers. If not, returns True
    if s.isalpha():
        return True
    else:
        #A variable to split the Plate in two, if there is a number
        splited_plate = []
        for element in s:
            #We'll verify if the first number is 0. In this case, the Plate won't be valid
            if element.isnumeric() and int(element) == 0:
                return False
            elif element.isnumeric():
                splited_plate = s.split(element)
                break
        #This variable is the second half of the Plate, witch has to be all numerical to be valid and return True, or have nothing, if there is a single number at the end (not 0)
        sec_half = str(splited_plate[1])
        return True if sec_half.isnumeric() or sec_half == "" else False


def is_alphanumerical(s):
    return True if s.isalnum() else False


if __name__ == "__main__":
    main()
