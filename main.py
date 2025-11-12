def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def count_words(book):
    words = book.split()
    return len(words)   

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words_in_book = count_words(book_text)
    print(f"Found {num_words_in_book} total words")

main()
