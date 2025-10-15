# 🐍 Sentimental Readability — CS50x Week 6

**Goal:** Reimplement the readability problem from Week 2 in Python to compute the Coleman–Liau index of a text and estimate its U.S. grade level.

---

### 🧠 Key Concepts
- Reading and processing user input  
- Counting letters, words, and sentences  
- Using loops and conditions in Python  
- String manipulation and arithmetic  
- Rewriting C logic in a higher-level language  

---

### ⚙️ Example Run
Text: Congratulations! Today is your day.
Grade 3

yaml
Copiar código

---

### 🧩 Core Formula
index = 0.0588 * L - 0.296 * S - 15.8

yaml
Copiar código
Where  
- **L** = average number of letters per 100 words  
- **S** = average number of sentences per 100 words  

---

### 💡 What I Learned

How to translate logic from C to Python, handle strings and loops efficiently, and write cleaner, more readable code.