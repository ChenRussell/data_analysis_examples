from nltk import word_tokenize
from nltk import Text

tokens = word_tokenize("Here is some not very interesting text")
print(type(tokens))
print(tokens)
text = Text(tokens)
print(type(text))
print(text)