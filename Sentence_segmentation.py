import spacy

nlp = spacy.load("en_core_web_sm")

doc = nlp("""Thinking about hospitalization but terrified. I don't know what to do. I lie in bed all day and I can't get myself to do anything, and I feel like I'm close to suicide. But I'm terrified of going to a hospital. I have medicaid and the only hospital in my county that accepts it is kind of a shitty hospital. I'm kind of afraid of hospitals to begin with so it doesn't help. I have an image in my head of going to a crowded dirty ward and being forgotten, or being given shitty medication that isn't right for me. A friend of mine was hospitalized once on a 72 hour hold, and she ended up sleeping on a gurney in a hallway the whole time (different hospital). I don't want to be in a strange place with strange people. I already feel alone and defective and I feel like being in a hospital will just make me feel like even more of a fuck up.  I need help, but I don't know what the right step is. I'm meeting with my school therapist tomorrow to talk through some options, but I guess I'm posting because I wanted to have some ideas when I talk to her.""")

#Segmentación método 1

assert doc.has_annotation("SENT_START")
for sent in doc.sents:
    print(sent.text)


#Segmentación método 2

from spacy.language import Language
import spacy

text = """Thinking about hospitalization but terrified. I don't know what to do. I lie in bed all day and I can't get myself to do anything, and I feel like I'm close to suicide. But I'm terrified of going to a hospital. I have medicaid and the only hospital in my county that accepts it is kind of a shitty hospital. I'm kind of afraid of hospitals to begin with so it doesn't help. I have an image in my head of going to a crowded dirty ward and being forgotten, or being given shitty medication that isn't right for me. A friend of mine was hospitalized once on a 72 hour hold, and she ended up sleeping on a gurney in a hallway the whole time (different hospital). I don't want to be in a strange place with strange people. I already feel alone and defective and I feel like being in a hospital will just make me feel like even more of a fuck up.  I need help, but I don't know what the right step is. I'm meeting with my school therapist tomorrow to talk through some options, but I guess I'm posting because I wanted to have some ideas when I talk to her."""


nlp = spacy.load("en_core_web_sm")
doc = nlp(text)
print("Before:", [sent.text for sent in doc.sents])

@Language.component("set_custom_boundaries")
def set_custom_boundaries(doc):
    for token in doc[:-1]:
        if token.text == "and":
            doc[token.i + 1].is_sent_start = True
    return doc

nlp.add_pipe("set_custom_boundaries", before="parser")
doc = nlp(text)
print("After:", [sent.text for sent in doc.sents])

#Segmentación método 3

import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Thinking about hospitalization but terrified. I don't know what to do. I lie in bed all day and I can't get myself to do anything, and I feel like I'm close to suicide. But I'm terrified of going to a hospital. I have medicaid and the only hospital in my county that accepts it is kind of a shitty hospital. I'm kind of afraid of hospitals to begin with so it doesn't help. I have an image in my head of going to a crowded dirty ward and being forgotten, or being given shitty medication that isn't right for me. A friend of mine was hospitalized once on a 72 hour hold, and she ended up sleeping on a gurney in a hallway the whole time (different hospital). I don't want to be in a strange place with strange people. I already feel alone and defective and I feel like being in a hospital will just make me feel like even more of a fuck up.  I need help, but I don't know what the right step is. I'm meeting with my school therapist tomorrow to talk through some options, but I guess I'm posting because I wanted to have some ideas when I talk to her.")
for sent in doc.sents:
    print(sent.text)

