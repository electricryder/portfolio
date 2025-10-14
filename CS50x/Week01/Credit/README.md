@"
# 💳 Credit — CS50x Week 1

**Goal:** Determine if a credit card number is valid using the **Luhn checksum**, and identify the issuer (AMEX, MasterCard, VISA).

**Key concepts:**
- Loops and integer arithmetic
- Modulo / division to traverse digits
- Input validation and branching logic

**How it works (Luhn in short):**
1. Starting from the last digit, double every other digit.
2. If doubling gives a two-digit number, sum those digits.
3. Add the untouched digits.
4. If the total ends in 0 → number is valid.

Ex:
Number: 4003600000000014 → VALID (VISA)

**Compile & run (CS50 environment):**
```bash
make credit
./credit