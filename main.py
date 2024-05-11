def main():
    book = "books/frankenstein.txt"
    text = get_book_text(book)
    nb_words = count_words(text)
    list_chars = count_char(text)
    sorted_list_chars = print_report(list_chars)
    print(f"--- Begin report of {book} ---")
    print(f"{nb_words} words found in the document")
    print()
    for item in sorted_list_chars:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

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

def sort_on(dict):
    return dict["num"]
 
def print_report(dict_char):
    list_char = []
    for char, value in dict_char.items():
        if char.isalpha():
            list_char.append({"char":char, "num":value})
    list_char.sort(reverse=True, key=sort_on)
    
    return list_char
        

main()

