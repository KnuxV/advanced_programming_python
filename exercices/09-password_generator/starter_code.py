import random
from pathlib import Path

# Configuration constants
N = 5  # Number of words in the password
SEP = " "  # Separator between words

# Path to word list file
# Path(__file__).parent represents the path of the file we are working with
# Even if we execute the script from somewhere else, for ex. the root of the projects this will work.
WORDS_PATH = Path(__file__).parent / "data" / "wordlist.txt"


def generate_password(num_words=N, separator=SEP):
    """Generate a password using random words from the word list.

    Args:
        num_words (int): Number of words to include in the password
        separator (str): String to use between words

    Returns:
        str: The generated password
    """
    # Load word list from file
    with open(WORDS_PATH, "r", encoding="utf-8") as f:
        lst_words = [w.strip() for w in f.readlines()]

    # Generate password by randomly sampling words without replacement
    # random.sample() ensures each word appears only once in the password
    result = random.sample(lst_words, k=num_words)

    # Join words with separator
    return separator.join(result)


if __name__ == "__main__":
    # Load word list to show basic info
    with open(WORDS_PATH, "r", encoding="utf-8") as f:
        lst_words = [w.strip() for w in f.readlines()]

    print(f"Loaded {len(lst_words)} words")
    print("First 5 words:", lst_words[:5])

    # Generate and display password
    password = generate_password(num_words=N, separator=" ")
    print(password)