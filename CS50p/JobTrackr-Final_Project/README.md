# JobTrackr
### CS50P Final Project — Pedro Rodrigues
### Video Demo: https://youtu.be/XpcvMToD5Vg

---

## 📌 Description

JobTrackr is a command-line job application manager written in Python for my CS50P Final Project. Its purpose is to help users track, organize, and review their job applications using a simple yet well-structured terminal interface. The program allows users to add new jobs, list all applications, update their statuses, search by keyword, generate summary reports, and delete entries — all while storing data persistently in a JSON file.

The goal of this project was not only to build a useful real-world tool but also to demonstrate object-oriented design, file I/O, modular structuring, error handling, and the testing skills required by the course. JobTrackr is entirely built in Python with no external dependencies.

I chose this project because I am personally in a phase of actively applying for software development roles, and having a tool like this genuinely helps me stay organized and track my progress.

---

## 🧩 Project Structure

The project is divided into multiple Python files plus a data directory:

```
project/
│
├── project.py          # Main program, menu logic, and standalone functions
├── tracker.py          # Tracker class: core logic + persistence layer
├── job.py              # Job class: represents a single application
├── test_project.py     # Pytest tests for standalone functions
├── requirements.txt    # Empty (no external libraries required)
│
└── data/
    └── jobs.json       # Local JSON "database" for storing jobs
```

This modular structure keeps components cleanly separated, improves readability, and makes future maintenance easier.

---

## 🧠 Design Decisions

### **Object-Oriented Approach**
The application uses two classes:
- **Job** — a data model for a single job application
- **Tracker** — manages all operations such as loading/saving JSON, searching, updating, and deleting jobs

### **Standalone Functions (required by CS50P)**
The standalone functions in `project.py` are:
- `count_jobs(tracker)`
- `search_keyword(tracker, keyword)`
- `count_by_status(tracker, status)`

They are pure, testable, and independent from user input.

### **Data Storage**
All data is stored in a JSON file (`data/jobs.json`) because it is simple, portable, and readable.

### **User Interface**
A clean, menu-driven command-line interface ensures accessibility and clarity.

---

## 🧪 Testing (pytest)

The file `test_project.py` includes tests for:

- `test_count_jobs()`
- `test_search_keyword()`
- `test_count_by_status()`

Run tests using:

```bash
pytest -q
```

All tests should pass successfully.

---

## 🚀 How to Run the Program

1. Install Python 3
2. Navigate to the project directory
3. Run:

```bash
python project.py
```

Use the menu to:
- Add jobs
- List jobs
- Update their status
- Search
- Generate reports
- Delete entries

---

## 📊 Features Summary

- Add new job entries
- List all job applications
- Update job statuses
- Delete jobs by ID
- Search by keyword
- Status-based reports
- JSON persistence
- Pytest test suite
- Modular architecture

---

## 🎬 Video Demo

**Video:** https://youtu.be/XpcvMToD5Vg

---

## 🏁 Conclusion

JobTrackr is a complete Python application that demonstrates OOP, file I/O, JSON handling, loops, exception management, external testing with pytest, and a modular project architecture. It is fully functional and genuinely useful for managing job applications in real life.

All code was written by Pedro Rodrigues.
