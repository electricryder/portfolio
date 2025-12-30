import pytest
from project import count_jobs, search_keyword, count_by_status
from tracker import Tracker
from job import Job


@pytest.fixture
def sample_tracker():
    tracker = Tracker()
    # Ignore any loaded data and use a controlled sample
    tracker.jobs = [
        Job(1, "CGI", "Python Developer", "2025-10-07", "Pending", ""),
        Job(2, "Nokia", "Software Engineer", "2025-02-14", "Interview", ""),
        Job(3, "Siemens", "ackend Developer", "2025-03-21", "Pending", ""),
    ]
    return tracker


def test_count_jobs(sample_tracker):
    assert count_jobs(sample_tracker) == 3


def test_search_keyword(sample_tracker):
    results = search_keyword(sample_tracker, "developer")
    # "Python Developer" and "Backend Developer"
    assert len(results) == 2
    assert any(job.company == "CGI" for job in results)
    assert any(job.company == "Siemens" for job in results)


def test_count_by_status(sample_tracker):
    assert count_by_status(sample_tracker, "pending") == 2
    assert count_by_status(sample_tracker, "interview") == 1
    assert count_by_status(sample_tracker, "rejected") == 0
