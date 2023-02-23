import spacy
import csv
import json


with open('suicide_corpus.json', 'r') as file:
    dic_data = json.load(file)

examples_values = dic_data['examples']

list_data = [value for value in examples_values]

#Convert the list into a str element

separador = """ ", """

string = separador.join(map(str, list_data))


#Segmentate each element of the list in sentences

nlp = spacy.load("en_core_web_sm")

doc = nlp(string)

#Segmentate into sentences 

assert doc.has_annotation("SENT_START")
results = []
for sent in doc.sents:
    results.append([sent.text])

#Save response as a csv

with open("sentences.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(results)










