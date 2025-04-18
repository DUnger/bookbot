def get_num_words(book_text):
    text_list = book_text.split()
    num_words = len(text_list)
    return num_words

def count_num_chars_dict(book_text):
    chars_dict = {}
    for char_origin in book_text:
        char = char_origin.lower()
        if char == " ":
            continue
        elif char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict
