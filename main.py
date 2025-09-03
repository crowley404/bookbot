import sys
from stats import get_num_words, get_all_characters

def import_book():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    return sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    path = import_book()
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    text = get_book_text(path)
    num_words = get_num_words(text)
    character_count = get_all_characters(text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in character_count:
        c = item["char"]
        n = item["num"]
        print(f"{c}: {n}")
    print("============= END ===============")

main()
