def main():
    with open("/home/jojo/workspace/github.com/jdemum/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
    word_count = wordcount(file_contents)
    print(f"{word_count} words found in the document")

def wordcount(file_contents):
    words = file_contents.split()
    num_words = len(words)
    return num_words
main()
