"""
CS50P Final Project
Pedro Rodrigues

JobTrackr - Application to manage and track job applications.

This program allows the user to add, update and list job applications,
storing all data in a JSON file for persistence.
"""

from tracker import Tracker
from time import sleep
import sys

# --- Standalone Functions (for CS50P + tests) --- #

def count_jobs(tracker):
    """
    Return the total number of jobs in the tracker.

    Args:
        tracker (Tracker): An instance of Tracker.

    Returns:
        int: Number of jobs stored in the tracker.
    """
    return len(tracker.jobs)


def search_keyword(tracker, keyword):
    """
    Return a list of jobs whose fields contain the given keyword.

    The search is case-insensitive and looks into:
    company, position, status, and notes.

    Args:
        tracker (Tracker): An instance of Tracker.
        keyword (str): The keyword to search for.

    Returns:
        list[Job]: List of Job objects matching the keyword.
    """
    keyword = keyword.lower()
    results = []

    for job in tracker.jobs:
        if (
            keyword in job.company.lower()
            or keyword in job.position.lower()
            or keyword in job.status.lower()
            or keyword in job.notes.lower()
        ):
            results.append(job)

    return results


def count_by_status(tracker, status):
    """
    Count how many jobs in the tracker match a given status.

    Args:
        tracker (Tracker): An instance of Tracker.
        status (str): Status to count (e.g., "Pending", "Interview").

    Returns:
        int: Number of jobs with the given status.
    """
    status = status.lower()
    return sum(1 for job in tracker.jobs if job.status.lower() == status)


def main():
    """
    Main function: runs the JobTrackr CLI application.
    """
    tracker = Tracker()

    print("Welcome to JobTrackr!")

    while True:
        print("\n--- MENU ---")
        print("[1] Add new Job")
        print("[2] List all Jobs")
        print("[3] Update Job Status")
        print("[4] Search Jobs")
        print("[5] Generate Report")
        print("[6] Delete Job")
        print("[7] Exit")

        try:
            opt = int(input("> "))
        except ValueError:
            print("Please, enter a valid number.")
            continue

        if opt == 1:
            tracker.add_job()

        elif opt == 2:
            if not tracker.jobs:
                print("\nNo jobs found!")
            else:
                print("\n--- All Jobs ---")
                for job in tracker.jobs:
                    print(job)

        elif opt == 3:
            tracker.update_status()

        elif opt == 4:
            tracker.search_jobs()

        elif opt == 5:
            tracker.generate_report()

        elif opt == 6:
            tracker.delete_job()

        elif opt == 7:
            print("Exiting", end="", flush=True)
            for _ in range(3):
                sleep(1)
                sys.stdout.write(".")
                sys.stdout.flush()
            sleep(1)
            print()
            break

        else:
            print("\nInvalid option!")


if __name__ == "__main__":
    main()
