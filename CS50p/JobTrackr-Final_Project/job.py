"""
job.py
Defines the Job class, representing a single job application.
"""

class Job:
    def __init__(self, id: int, company: str, position: str, date: str, status: str, notes: str = ""):
        """
        Initialize a Job instance.

        Args:
            id (int): Unique identifier for the job.
            company (str): Name of the company.
            position (str): Position or title applied for.
            date (str): Date of application (YYYY-MM-DD).
            status (str): Current status (e.g.: Pending, Interview, Rejected, Accepted).
            notes (str, optional): Additional notes. Defaults to empty string "".
        """
        self.id = id
        self.company = company
        self.position = position
        self.date = date
        self.status = status
        self.notes = notes

    def to_dict(self) -> dict:
        """
        Convert the Job instance into a dictionary.

        Returns:
            dict: A dictionary representation of the job.
        """
        return {
            "id": self.id,
            "company": self.company,
            "position": self.position,
            "date": self.date,
            "status": self.status,
            "notes": self.notes
        }

    def __str__(self) -> str:
        """
        Return a human-readable string to represent the job.
        """
        return f"Job ID: [{self.id}] {self.company} - {self.position} ({self.status})"
