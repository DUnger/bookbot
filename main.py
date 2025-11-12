from stats import get_num_words

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words_in_book = get_num_words(book_text)
    print(f"Found {num_words_in_book} total words")

main()
