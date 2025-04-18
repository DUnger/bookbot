from stats import get_num_words

file_path = "books/frankenstein.txt"

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_text = get_book_text(file_path)
    num_words = get_num_words(book_text)
    print(f"{num_words} words found in the document")


main()
