import sys
from stats import count_words, count_characters


def get_book_text (path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    
    #path = "books/frankenstein.txt"
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    count_words(path)
    print("--------- Character Count -------")
    char_list = count_characters(path)
    for item in char_list:
        ch = item["char"]
        num = item["num"]
        print(f"{ch}: {num}")
    print("============= END ===============")
    
main()
