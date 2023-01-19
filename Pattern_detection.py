#Solución posible a la detección de frases verbales. 

import spacy
import textacy

nlp = spacy.load('en_core_web_sm')

doc = nlp("""Thinking about hospitalization but terrified. I don't know what to do. I lie in bed all day and I can't get myself to do anything, and I feel like I'm close to suicide. But I'm terrified of going to a hospital. I have medicaid and the only hospital in my county that accepts it is kind of a shitty hospital. I'm kind of afraid of hospitals to begin with so it doesn't help. I have an image in my head of going to a crowded dirty ward and being forgotten, or being given shitty medication that isn't right for me. A friend of mine was hospitalized once on a 72 hour hold, and she ended up sleeping on a gurney in a hallway the whole time (different hospital). I don't want to be in a strange place with strange people. I already feel alone and defective and I feel like being in a hospital will just make me feel like even more of a fuck up.  I need help, but I don't know what the right step is. I'm meeting with my school therapist tomorrow to talk through some options, but I guess I'm posting because I wanted to have some ideas when I talk to her.""")
sentences = list(doc.sents)
sentence = (sentences[2])

#Deteccion de patrones de lenguaje

patterns = [[{"POS": "ADJ"},{"POS":"NOUN"}],[{"POS":"NOUN"}, {"POS":"ADJ"}]]

verbs_phrases = textacy.extract.token_matches(doc, patterns=patterns)

for verb_phrases in verbs_phrases:
    print(verb_phrases)

