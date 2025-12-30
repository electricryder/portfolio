"""
tracker.py
Defines the Tracker class, responsible for managing job applications.
"""
import json
import os
from job import Job


class Tracker:
    def __init__(self, data_file: str = "data/jobs.json"):
        """
        Initialize the Tracker with an empty list of jobs
        and load existing jobs from the data file if available.

        Args:
            data_file (str): Path to the JSON file used for saving and loading job data.
        """
        self.data_file = data_file
        self.jobs = []
        self.load_data()

    def load_data(self):
        """
        Reads jobs from the JSON file and loads them into self.jobs
        """
        if not os.path.exists(self.data_file):
            # If the file doesn't exist yet
            return

        try:
            with open(self.data_file, "r") as data_json_file:
                data = json.load(data_json_file)

                # Each item in 'data' is a dictionary
                for job_dict in data:
                    job = Job(
                        id=job_dict["id"],
                        company=job_dict["company"],
                        position=job_dict["position"],
                        date=job_dict["date"],
                        status=job_dict["status"],
                        notes=job_dict["notes"]
                    )
                    self.jobs.append(job)

        except (json.JSONDecodeError, FileNotFoundError):
            # Handle empty or invalid JSON file
            self.jobs = []

    def save_data(self):
        """
        Saves a list of jobs into the JSON file
        """
        data = []

        # Loop through all jobs and turn each into a dict
        for job in self.jobs:
            data.append(job.to_dict())

        # Writes the list of dictionaries to the JSON file
        with open(self.data_file, "w") as file:
            json.dump(data, file, indent=4)

    def add_job(self):
        """
        Prompts the user for job information and adds a new Job to the tracker.
        """
        print("\n--- Add New Job ---")
        company = input("Company name > ").strip()
        position = input("Position title > ").strip()
        date = input("Date of application (YYYY-MM-DD) > ").strip()
        status = input("Current status (Pending / Interview / Rejected / Accepted) > ").strip()
        notes = input("Additional notes (optional) > ").strip()

        # Automatically generate a new ID
        new_id = len(self.jobs) + 1

        new_job = Job(
            id=new_id,
            company=company,
            position=position,
            date=date,
            status=status,
            notes=notes
        )

        # Adds new job to the list
        self.jobs.append(new_job)

        # Saves it into the JSON file
        self.save_data()

        print(f"\n✅ Job added successfully! (ID: {new_job.id})")

    def update_status(self):
        """
        Allows the user to update the status of a job by its ID.
        """
        if not self.jobs:
            print("\nNo jobs available to update.")
            return

        print("\n--- Update Job Status ---")
        for job in self.jobs:
            print(job)

        try:
            job_id = int(input("\nEnter the Job ID to update: "))
        except ValueError:
            print("Invalid ID. Please enter a number.")
            return

        for job in self.jobs:
            if job.id == job_id:
                new_status = input("Enter new status (Pending / Interview / Rejected / Accepted): ").strip()
                job.status = new_status
                self.save_data()
                print(f"\n✅ Job ID {job_id} updated successfully!")
                return

        print(f"\nNo job found with ID {job_id}.")

    def search_jobs(self):
        """
        Allows the user to search jobs by keyword (company, position, status, or notes).
        """
        if not self.jobs:
            print("\nNo jobs to search.")
            return

        search_word = input("\nEnter a search keyword: ").strip().lower()

        print(f"\n--- Search Results for '{search_word}' ---")

        results = []
        for job in self.jobs:
            # We convert everything to lowercase so search is case-insensitive
            if (
                search_word in job.company.lower()
                or search_word in job.position.lower()
                or search_word in job.status.lower()
                or search_word in job.notes.lower()
            ):
                results.append(job)

        if not results:
            print("No matching jobs found.")
        else:
            for job in results:
                print(job)

    def generate_report(self):
        """
        Prints a summary report of all job applications by status.
        """
        if not self.jobs:
            print("\nNo jobs found!")
            return

        print("\n--- Jobs Report ---")

        total = len(self.jobs)
        pending = sum(1 for job in self.jobs if job.status.lower() == "pending")
        interview = sum(1 for job in self.jobs if job.status.lower() == "interview")
        rejected = sum(1 for job in self.jobs if job.status.lower() == "rejected")
        accepted = sum(1 for job in self.jobs if job.status.lower() == "accepted")

        print(f"Total jobs: {total}")
        print(f"Pending: {pending}")
        print(f"Interview: {interview}")
        print(f"Rejected: {rejected}")
        print(f"Accepted: {accepted}")

    def delete_job(self):
        """
        Deletes a job by its ID.
        """
        if not self.jobs:
            print("\nNo jobs available to delete.")
            return

        print("\n--- Delete Job ---")
        for job in self.jobs:
            print(job)

        try:
            job_id = int(input("\nEnter the Job ID to delete: "))
        except ValueError:
            print("Invalid ID. Please enter a number.")
            return

        for job in self.jobs:
            if job.id == job_id:
                self.jobs.remove(job)
                self.save_data()
                print(f"\n🗑️ Job ID {job_id} deleted successfully!")
                return

        print(f"\n⚠️ No job found with ID {job_id}.")
