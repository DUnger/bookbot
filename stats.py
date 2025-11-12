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

def sort_on(items):
    return items["num"]

def get_sorted_list_dicts(chars_dict):
    sorted_list = []
    for char in chars_dict:
        sorted_list.append({"char": char, "num": chars_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
