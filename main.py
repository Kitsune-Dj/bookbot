import string

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    char_counts = get_num_chars(text)
    sorted_chars = sorted(char_counts.items(), key=lambda item: (-item[1], item[0]))
    """
    char_counts counts the amount of times a character shows up in a .txt file
    sorted_chars gets character counts and sorts them in order of frequency in decending order
    """
    print(f"--Starting report of {book_path}--")
    print(f"{num_words} words found in the document")
    #Prints character counts
    for char, count in sorted_chars:
        print(f"the '{char}' character was found {count} times")
    print(f"--End of current report--")
    #A loop thar will print a report of a .txt file letting you know the word count and how many times a character shows up
    


def get_num_words(text):
    """
    Returns the word count for a .txt file
    """
    words = text.split()
    return len(words)  

def get_num_chars(text): 
    """
    Returns the amount unique characters that are in a .txt file
    Also converts all characters to lowercase
    """
    valid_chars = list(string.ascii_lowercase)

    chars = {}
    for c in text:
     lowered = c.lower()
     if lowered in valid_chars:   
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars
    



       



def get_book_text(path):
    with open(path) as f:
        return f.read()

main()


