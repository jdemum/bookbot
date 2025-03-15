from stats import get_num_words
from stats import char_count
from stats import sort_char_count  # Import your new function
import sys 

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1) 
book_path = sys.argv[1]

def main():
    with open(book_path) as f:
        file_contents = f.read()
    word_count = get_num_words(file_contents)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    
    char_counts = char_count(file_contents)
    sorted_counts = sort_char_count(char_counts)  # Use your new function
    
    print("--------- Character Count -------")
    for char_dict in sorted_counts:
        if char_dict["char"].isalpha():
            print(f"{char_dict['char']}: {char_dict['count']}")
    
    print("============= END ===============")

main()
