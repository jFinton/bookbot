def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    sorted_list = dict_to_sorted_list(get_letter_count(book_text))
    print(f"--- Beginning report of {book_path} ---")
    print(f" There are {get_word_count(book_text)} words found in this document. ")
    print()

    for letter in sorted_list:
        if letter["letter"].isalpha():
            print(f"The '{letter["letter"]}' character was found {letter["count"]} times")
    
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def get_letter_count(text):
    letter_dict = {}
    lower_text = text.lower()
    for letter in lower_text:
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1
    return letter_dict

def sort_on(dict):
    return dict["count"]

def dict_to_sorted_list(dict):
    sorted_list = []
    for letter in dict:
        sorted_list.append({"letter": letter, "count": dict[letter]})
    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list

main()