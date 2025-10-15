import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    hour_in = valid_input(s)
    hour = valid_hour(hour_in)
    return hour


def valid_input(inpt):
    inpt_str = inpt.split(" ")
    if len(inpt_str) != 5:
        raise ValueError
    if inpt_str[2] != "to":
        raise ValueError
    if inpt_str[1] != "AM" and inpt_str[1] != "PM":
        raise ValueError
    if inpt_str[4] != "AM" and inpt_str[4] != "PM":
        raise ValueError
    else:
        hour = str(
            f"{inpt_str[0]} {inpt_str[1]} {inpt_str[2]} {inpt_str[3]} {inpt_str[4]}"
        )
    return hour


'''def valid_args():
    if len(sys.argv) < 6:
        raise ValueError
    if len(sys.argv) > 6:
        raise ValueError
    if sys.argv[3] != "to":
        raise ValueError
    if sys.argv[2] != "AM" and sys.argv[2] != "PM":
        raise ValueError
    if sys.argv[5] != "AM" and sys.argv[5] != "PM":
        raise ValueError
    else:
        hour = str(
            f"{sys.argv[1]} {sys.argv[2]} {sys.argv[3]} {sys.argv[4]} {sys.argv[5]}"
        )
        return hour'''


def valid_hour(s):
    if matches := re.search(
        r"((?:\w+)(?:\:\w+)?)( AM| PM) to ((?:\w+)(?:\:\w+)?)( AM| PM)", s
    ):
        init_hour = str_splitter(matches.group(1)) + matches.group(2)
        final_hour = str_splitter(matches.group(3)) + matches.group(4)
        return f"{arranger(init_hour)} to {arranger(final_hour)}"


def str_splitter(s):
    if len(s.split(":")) == 2:
        hour = int(s.split(":")[0])
        minute = int(s.split(":")[1])
        if hour < 1 or hour > 12 or 0 < minute > 59:
            raise ValueError
        else:
            return f"{hour:02}:{minute:02}"
    else:
        hour = int(s)
        if hour < 1 or hour > 12:
            raise ValueError

        minute = 0
        return f"{hour:02}:{minute:02}"


def arranger(s):
    time = s.split(" ")[0]
    index = s.split(" ")[1]
    if index == "PM":
        if int(time.split(":")[0]) == 12:
            return f"{time.split(":")[0]:02}:{time.split(":")[1]:02}"
        else:
            new_hour = int(time.split(":")[0]) + 12
            return f"{new_hour:02}:{time.split(":")[1]:02}"
    elif index == "AM":
        if int(time.split(":")[0]) == 12:
            new_hour = 0
            return f"{new_hour:02}:{time.split(":")[1]:02}"
        return s.replace(" AM", "")


if __name__ == "__main__":
    main()
