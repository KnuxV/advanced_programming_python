import random
from pathlib import Path

# Configuration constants
N = 5  # Number of words in the password
SEP = " "  # Separator between words

# Path to word list file
# Path(".") gets the current directory, .parent goes up one level
# Alternative: you could use os.getcwd() or pathlib.Path.cwd()
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
    import sys

    # we must have 2 argument, the name of the script and the number of words
    if len(sys.argv) != 2:
        print("python password_gen_argv.py 4")
        sys.exit()

    try:
        num_words = int(sys.argv[1])
    except ValueError:
        print("Error: Please provide a valid number")
        print("Usage: python password_gen_argv.py <number_of_words>")
        sys.exit()

    num_words = num_words if 11 > num_words > 0 else 5

    # Load word list to show basic info
    with open(WORDS_PATH, "r", encoding="utf-8") as f:
        lst_words = [w.strip() for w in f.readlines()]

    print(f"Loaded {len(lst_words)} words")
    print("First 5 words:", lst_words[:5])

    # Generate and display password
    password = generate_password(num_words=num_words, separator=" ")
    print(password)