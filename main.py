from stats import get_num_words, get_num_chars_dict, sort_chars_dict
import sys



def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def print_report(book_path, num_words, sorted_chars_dict_list):
    print("============ BOOKBOT ============")
    print("Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for dict in sorted_chars_dict_list:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]}")
    
    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    num_words = get_num_words(book_text)
    chars_dict = get_num_chars_dict(book_text)
    sorted_chars_dict_list = sort_chars_dict(chars_dict)
    print_report(file_path, num_words, sorted_chars_dict_list)    

main()
