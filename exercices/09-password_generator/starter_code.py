import random
from pathlib import Path

# Configuration constants
N = 5  # Number of words in the password
SEP = " "  # Separator between words

# Path to word list file
# Path(".") gets the current directory, .parent goes up one level
# Alternative: you could use os.getcwd() or pathlib.Path.cwd()
WORDS_PATH = Path(".") / "data" / "wordlist.txt"

# Load word list from file
with open(WORDS_PATH, "r", encoding="utf-8") as f:
    lst_words = [w.strip() for w in f.readlines()]

print(f"Loaded {len(lst_words)} words")
print("First 5 words:", lst_words[:5])

# Generate password by randomly sampling words without replacement
# random.sample() ensures each word appears only once in the password
result = random.sample(lst_words, k=N)

if __name__ == '__main__':

# Join words with separator
password = SEP.join(result)
print(f"Generated password: {password}")