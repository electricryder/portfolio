import sys
import csv


def main():
    chosen_file = valid_args()
    scourgify(chosen_file)


def valid_args():
    if len(sys.argv) == 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1][-4:] != ".csv" and sys.argv[2][-4:] != ".csv":
            sys.exit("Not both CSV files")
        else:
            students_list = sys.argv[1]
    try:
        with open(students_list) as file:
            return sys.argv[1]
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")


def scourgify(list_file):

    students = []

    # Reading File
    with open(list_file) as file:
        reader = csv.DictReader(file)
        for row in reader:
            student_name_sep = row["name"].split(",")
            students.append(
                {
                    "first": student_name_sep[1].strip(),
                    "last": student_name_sep[0],
                    "house": row["house"],
                }
            )

    # Writing File
    with open(f"{sys.argv[2]}", "w") as file:
        writer = csv.DictWriter(file, fieldnames= ["first", "last", "house"])
        writer.writeheader()
        for row in students:
            writer.writerow(row)


if __name__ == "__main__":
    main()
