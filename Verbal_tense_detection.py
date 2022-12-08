import pandas as pd
import nltk 

from nltk import word_tokenize
from nltk import pos_tag

def determine_tense_input(sentence):
    #bigrm = list(nltk.bigrams(sentence.split()))
    #list = [' '.join(x) for x in bigrm]
    text = word_tokenize(sentence)
    tagged = pos_tag(sentence)

    tense = {}
    tense["future"] = len([word for word in tagged if word[1] == "MD"]) #This is a for cycle written in one line? If so, what does it mean the '1' in brackets?
    tense["present"] = len([word for word in tagged if word[1] in ["VBP", "VBZ","VBG"]]) #These categories are in useful_links document
    tense["past"] = len([word for word in tagged if word[1] in ["VBD", "VBN","VHN"]]) #VHN
    return(tense)