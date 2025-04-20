from stats import get_num_words, get_num_chars_dict, sort_chars_dict



def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    file_path = "books/frankenstein.txt"
    book_text = get_book_text(file_path)
    num_words = get_num_words(book_text)
    chars_dict = get_num_chars_dict(book_text)
    sorted_chars_dict_list = sort_chars_dict(chars_dict)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for dict in sorted_chars_dict_list:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]}")
    
    print("============= END ===============")

main()
