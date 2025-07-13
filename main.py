from stats import (
    get_word_count,
    get_character_counts,
    sort_character_counts,
)
import sys



def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        text_file = sys.argv[1]
        full_text = get_book_text(text_file)
        num_words = get_word_count(full_text)
        char_dict = get_character_counts(full_text)
        sorted_char_list = sort_character_counts(char_dict)
        print_report(text_file, num_words, sorted_char_list)


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def print_report(book_path, num_words, sorted_char_list):
    print("============ BOOKBOT ============")
    (f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in sorted_char_list:
        print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")



main()