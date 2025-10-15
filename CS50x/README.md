# 🧠 CS50x – Selected Exercises & Projects

This folder contains a **curated selection** of my solutions from **CS50x: Introduction to Computer Science (Harvard)**.
The goal is to show fundamentals: algorithms, data structures, memory, Python, and SQL.

## 📁 Structure
Each `WeekXX` directory will contain exercises with:
- Source files (`.c`, `.py`, `.sql`, etc.)
- A short `README.md` per exercise: problem summary, approach, and how to run.

Suggested mapping (you can adjust):
- `Week01` – C basics (loops/conditions) – *Mario, Cash*
- `Week02` – Arrays – *Readability*
- `Week03` – Algorithms – *Plurality*
- `Week04` – Memory – *Filter, Recover*
- `Week05` – Data Structures – *Speller*
- `Week06` – Python – *Sentimental Mario/Readability*
- `Week07` – SQL – *Movies*
- `Week08` – Web (HTML | CSS | JavaScript) – *Homepage*
- `Week09` – Flask
- `Week10` – Final Project

## ▶️ Running examples

### C (locally)
You can compile with GCC if installed:
```bash
gcc -o program program.c
./program
```
Or use the CS50 online environment.

### Python
```bash
python file.py
```

### Flask (Week08/Project)
```bash
pip install -r requirements.txt
flask --app app.py --debug run
```

## 📝 Per-exercise README template
Copy this into each exercise folder:
```markdown
# Exercise: <Name>
**Problem:** Short summary of what the exercise asks.
**Approach:** Key idea(s), data structures, and trade-offs.
**How to run:** Commands / inputs / expected outputs.
**Notes:** Edge cases, improvements, or what I learned.
```
