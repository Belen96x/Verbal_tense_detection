import spacy

nlp = spacy.load("en_core_web_sm")

import spacy

nlp = spacy.load("en_core_web_sm")

def segment_sentence(text):
    doc = nlp(text)
    clauses = []
    start_index = 0
    
    for token in doc:
        # Check if the token is a conjunction that separates clauses
        if token.dep_ == "cc" or token.dep_ == "mark":
            # Add the current clause to the list
            clause = doc[start_index:token.i+1]
            clauses.append(clause)
            start_index = token.i+1
    
    # Add the last clause to the list
    clause = doc[start_index:]
    clauses.append(clause)
    
    return clauses



#Lets try it

text = "I said it was a plan and then they *said that I had the drugs in my backpack*.they quickly called a ambulance to get me out of there and put me there without my will The crisis center was terrible."
clauses = segment_sentence(text)

for clause in clauses:
    print(clause.text)
