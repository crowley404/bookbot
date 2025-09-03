def get_book_text(filepath) :
	with open(filepath) as f:
		file_contents = f.read()
	return file_contents

from stats import get_num_words

from stats import get_num_characters

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_characters = get_num_characters(text)
    print(f"{num_words} words found in the document")
    print(num_characters)

main()
