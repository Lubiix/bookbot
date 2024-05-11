def main():
    book = "books/frankenstein.txt"
    text = get_book_text(book)
    nb_words = count_words(text)
    print(f"There is {nb_words} dans {book}")
    list_letters = count_letters(text)
    print(list_chars)

def count_words(text):
    count = len(text.split())
    return count

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def count_char(text):
    count_char = {};
    text_lower = text.lower()
    for char in text_lower:
        if char in count_char:
            count_char[char] += 1
        else:
            count_char[char] = 1
    return count_char
    

main()

