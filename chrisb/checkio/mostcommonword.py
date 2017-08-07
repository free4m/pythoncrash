#!/usr/bin/python

import operator
from string import maketrans

def get_count(word_counts):
  return word_counts[1]

def checkio(text):
    word_count = {}
    text = text.translate(str.maketrans('','',"!?.,'123456789"))
    text = text.replace(" ","")
    words = list(text.lower())
    for word in words:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] = word_count[word] + 1
            
    top_word = sorted(word_count.items(), key=operator.itemgetter(0), reverse=True)
    print(top_word)
    
    for i in top_word[:1]:
        return(i[0])
        

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
