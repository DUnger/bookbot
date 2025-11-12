from stats import get_num_words, get_num_chars, get_sorted_list_dicts
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(sys.argv[1])
    num_words_in_book = get_num_words(book_text)
    chars = get_num_chars(book_text)
    sorted_list = get_sorted_list_dicts(chars)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words_in_book} total words")
    print("--------- Character Count -------")

    for dict in sorted_list:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]}")

    print("============= END ===============")

main()
