def get_num_words(book):
    words = book.split()
    return len(words)  

def get_num_chars(book):
    chars = {}
    for char in book:
        lower_char = char.lower()
        if lower_char in chars:
            chars[lower_char] +=1
        else:
            chars[lower_char] = 1
    return chars 
