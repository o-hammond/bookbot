def get_word_count(book_text):
    words = book_text.split()
    return len(words)


def get_character_counts(book_text):
    # for all characters in string
    # make character lower case
    # if key doesn't exist, add it to dict
    # if key does exist, add 1 to count
    text_lower_case = book_text.lower()
    counts = {}
    for char in text_lower_case:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts


def sort_on(items):
    return items["num"]


def sort_character_counts(character_dict):
    sorted_list = []
    for key in character_dict:
        if key.isalpha():
            sorted_list.append({"char": key,
                                "num": character_dict[key]})
    # sort list by num
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

