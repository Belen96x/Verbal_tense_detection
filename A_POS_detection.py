#Trying to determine the POS structure of the corpus

import nltk

text ="I will kill myself"

tokens = nltk.word_tokenize(text)
pos_tags = nltk.pos_tag(tokens)

print(pos_tags)