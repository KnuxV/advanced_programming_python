import argparse
import random
from pathlib import Path

# Configuration constants
N = 5  # Number of words in the password
SEP = " "  # Separator between words

# Path to word list file
# Path(".") gets the current directory, .parent goes up one level
# Alternative: you could use os.getcwd() or pathlib.Path.cwd()
WORDS_PATH = Path(__file__).parent / "data" / "wordlist.txt"


def generate_password(num_words=N, separator=SEP, capitalize=False, add_digits=False):
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
    result: list[str] = random.sample(lst_words, k=num_words)

    if capitalize:
        result = [w.capitalize() for w in result]
    if add_digits:
        result = [f"{w}{random.randint(0,10)}" for w in result]

    # Join words with separator
    return separator.join(result)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Password generator")

    parser.add_argument(
        "-n", "--num-words",
        type=int,
        help="Number of words",
        default=5
    )
    parser.add_argument(
        "-s", "--separator",
        choices=['dash', 'space', 'underscore', "slash"],
        default='space',
        help="Choose a separator between dash, space, underscore and slash"
    )
    parser.add_argument("-c", "--capitalize", action="store_true")
    parser.add_argument("-d", "--add-digits", action="store_true")

    separator_map = {
        'space': ' ',
        'dash': '-',
        'underscore': '_',
        'slash': '/'
    }

    args = parser.parse_args()
    num_words = args.num_words
    sep = separator_map[args.separator]
    capitalize = args.capitalize
    add_digits = args.add_digits



    # Load word list to show basic info
    with open(WORDS_PATH, "r", encoding="utf-8") as f:
        lst_words = [w.strip() for w in f.readlines()]


    # Generate and display password
    password = generate_password(num_words=num_words, separator=sep, capitalize=capitalize, add_digits=add_digits)
    print(password)