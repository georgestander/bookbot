def main():
    path = "books/frankenstein.txt"
    text = book_path()
    num_words = count_words(text)
    num_chars = count_characters(text)
    sorted_list = sort_list(num_chars)

    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words found in the document. \n")
    for item in sorted_list:
        if item["char"].isalpha():
            print(f"The '{item['char']}' character was found {item['num']} times")
    print(f"--- End of report ---")

#get contents of the book
def book_path():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
    return file_contents

#count the number of words in the book
def count_words(text):
    words = text.split()
    return len(words)


#count the number of characters in the book
def count_characters(s):
    characters = {}
    for char in s:
        low_case = char.lower()
        if low_case in characters:
            characters[low_case] += 1
        else:
            characters[low_case] = 1
    return characters

#sort the characters in the book in a dictionary list
def sort_characters(dict):
    return dict["num"]

#sort the characters in the book in defined dictionary list
def sort_list(num_dict):
    sorted_list=[]
    for key in num_dict:
        sorted_list.append({"char": key, "num": num_dict[key]})
    sorted_list.sort(key=sort_characters, reverse=True)
    return sorted_list



    
    
    
main()