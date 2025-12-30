from cs50 import get_string

# Get a text
text = get_string("Text: ")

# Number of words
word = text.strip().split(" ")
n_words = len(word)

# Number of letters
n_letters = 0
for i in range(len(text)):
    if text[i].isalpha():
        n_letters += 1

# Number of sentences
n_sentences = 0
for i in range(len(text)):
    if text[i] == "." or text[1] == "!" or text[i] == "?":
        n_sentences += 1

# Coleman-Liau Index
L = (n_letters * 100.00) / n_words
S = (n_sentences * 100.00) / n_words
index = 0.0588 * L - 0.296 * S - 15.8

# Outputs
if index < 1:
    print("Before Grade 1")
elif index >= 16:
    print("Grade 16+")
else:
    print("Grade ", round(index))
