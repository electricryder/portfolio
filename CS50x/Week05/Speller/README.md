# 🧠 Speller — CS50x Week 5

**Goal:** Implement a spell-checking program that reads a dictionary into memory and checks the spelling of words in a text, using an efficient hash table.

---

### 🧠 Key Concepts
- Hash tables and linked lists for efficient lookups  
- File I/O (`fopen`, `fscanf`, `fclose`)  
- String manipulation (`strcmp`, `strcpy`, `tolower`)  
- Dynamic memory allocation (`malloc`, `free`)  
- Performance optimization (minimizing load, check, and unload times)

---

### ⚙️ Program Workflow
1. Load words from a dictionary file into memory  
2. Read a text file word-by-word  
3. Check each word’s spelling against the dictionary  
4. Output misspelled words and timing statistics  

---

### 🧩 Example Run

./speller dictionaries/large text.txt
MISSPELLED WORDS
mispelled
txtt
WORDS MISSPELLED: 2
WORDS IN DICTIONARY: 143091
WORDS IN TEXT: 1234
TIME IN load: 0.05
TIME IN check: 0.23
TIME IN size: 0.00
TIME IN unload: 0.03
TIME IN TOTAL: 0.31


---

### 💡 What I Learned
How hash tables work, how to manage memory dynamically, and how to measure algorithmic efficiency in real programs.