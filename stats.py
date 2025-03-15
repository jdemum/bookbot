def get_num_words(text):
    # Count and return the number of words in the text
    words = text.split()
    return len(words)

def char_count(text):
    # Count occurrences of each character in lowercase
    chars = {}
    for char in text.lower():
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def sort_on(dict):
    # Return the value to sort by
    return dict["count"]

def sort_char_count(char_dict):
    # Convert dictionary to list of dictionaries
    char_list = []
    for char, count in char_dict.items():
        char_list.append({"char": char, "count": count})
    # Sort the list by count in descending order
    char_list.sort(reverse=True, key=sort_on)
    return char_list