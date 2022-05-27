# Read text from a file, and count the occurrence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here
    with open(filename) as f:
        file = f.read()
    return file


def count_words():
    text = read_file_content("./story.txt")
    words_list = text.split(" ")
    word_dictionary = {}
    # [assignment] Add your code here
    for word in words_list:
        key, value = word, words_list.count(word)
        word_dictionary[key] = value
    print(word_dictionary)


count_words()
