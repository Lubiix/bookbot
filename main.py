def main():
    book = "books/frankenstein.txt"
    text = get_book_text(book)
    nb_words = count_words(text)
    print(f"There is {nb_words} dans {book}")
    list_letters = count_letters(text)
    print(list_letters)

def count_words(text):
    count = len(text.split())
    return count

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def count_letters(text):
    count_letter = {};
    text_lower = text.lower()
    for letter in text_lower:
        if letter in count_letter:
            count_letter[letter] += 1
        else:
            count_letter[letter] = 1
    return count_letter
    

main()

