def get_num_words(book_text):
    text_list = book_text.split()
    num_words = len(text_list)
    return num_words

def get_num_chars_dict(book_text):
    chars_dict = {}
    for char_origin in book_text:
        char = char_origin.lower()
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict

def sort_on(dict):
    return dict["num"]

def sort_chars_dict(chars_dict):
    dict_list = []
    for key in chars_dict:
        key_dict = {"char": key, "num": chars_dict[key]}
        dict_list.append(key_dict)  
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
