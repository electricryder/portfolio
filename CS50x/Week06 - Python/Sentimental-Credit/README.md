# 💳 Sentimental Credit — CS50x Week 6

**Goal:** Recreate the credit card validation program from Week 1 using Python, implementing Luhn’s Algorithm to determine if a number is a valid credit card.

---

### 🧠 Key Concepts
- Loops and conditionals in Python  
- Arithmetic with integers and digits  
- Slicing and iterating through strings  
- Applying **Luhn’s Algorithm** for checksum validation  
- Detecting card types (AMEX, MASTERCARD, VISA)

---

### ⚙️ Example Run

Number: 4003600000000014
VISA

Number: 61789372994
INVALID

---

### 🧩 Core Logic
1. Multiply every other digit by 2, starting from the second-to-last  
2. Add the sum of those digits to the sum of the remaining digits  
3. If the total’s last digit is 0 → valid  
4. Identify card type by starting digits + length  

---

### 💡 What I Learned
How to translate an algorithm from C to Python, use string operations for digit handling, and structure clear, concise Python functions.