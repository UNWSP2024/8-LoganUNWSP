#Logan H's Word Seperator
#
import re

def separate_words(no_space_sentence):
    words = re.findall(r'[A-Z][a-z]*', no_space_sentence)
    sentence = ' '.join(words).lower()
    return sentence.capitalize() + '.'

no_space_sentence = input("Enter a no-space sentence: ")
print("Converted sentence:", separate_words(no_space_sentence))
