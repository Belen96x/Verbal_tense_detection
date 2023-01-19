import pandas as pd
import nltk 

from nltk import word_tokenize
from nltk import pos_tag



#Determinar tiempo verbal

def determine_tense_input(sentence):
    text = word_tokenize(sentence)
    tagged = pos_tag(text)

    tense = {}
    tense["future"] = len([word for word in tagged if word[1] == "MD"]) #This is a for cycle written in one line? If so, what does it mean the '1' in brackets?
    tense["present"] = len([word for word in tagged if word[1] in ["VBP", "VBZ","VBG"]]) #These categories are in useful_links document
    tense["past"] = len([word for word in tagged if word[1] in ["VBD", "VBN","VHN"]]) #VHN
    return(tense)


phrases = ["it all ends tonight", "i will commit suicide", "i made a suicide attempt", "i used to have suicidal thoughts"]

prueba = list(map(determine_tense_input, phrases))

print(prueba)

#Aplicando grados de severidad

