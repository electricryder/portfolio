# 📖 Readability — CS50x Week 2

**Goal:** Implement a program that calculates the **reading grade level** of a text using the *Coleman–Liau index*.

**Key concepts:**
- Strings and character iteration  
- Counting letters, words, sentences  
- Arithmetic and rounding (float → int)  

**Formula:**  

index = 0.0588 × L – 0.296 × S – 15.8

where L = avg letters per 100 words, S = avg sentences per 100 words.

**Example:**

Text: Congratulations! Today is your day. You're off to Great Places! You're off and away!
Grade 3

**Compile & run (CS50 env):**
```bash
make readability
./readability

What I learned: Looping through strings in C, using conditionals to count characters, and applying a real-world formula programmatically.
