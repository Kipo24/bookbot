import sys

from stats import get_word_count, get_char_heatmap, get_sorted_char_heatmap


def get_book_text(filepath):
    text = None
    with open(filepath) as book_file:
        text = book_file.read()
    return text


def print_book_report(book_name, word_count, char_heatmap):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_name}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    sorted_char_heatmap = get_sorted_char_heatmap(char_heatmap)
    for char_count_pair in sorted_char_heatmap:
        char = char_count_pair["char"]
        count = char_count_pair["count"]
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_file_path = sys.argv[1]
    text = get_book_text(book_file_path)
    word_count = get_word_count(text)
    heatmap = get_char_heatmap(text)

    book_file_path_split = book_file_path.split("/")
    print_book_report(book_file_path_split[-1], word_count, heatmap)

    


main()
