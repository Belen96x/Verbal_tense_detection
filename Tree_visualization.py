import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Thinking about hospitalization but terrified.")
displacy.serve(doc, style="dep")