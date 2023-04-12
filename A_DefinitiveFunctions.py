#Import of libraries

import nltk
import spacy
import csv
import json
import pandas as pd
from nltk import pos_tag
from nltk.tokenize import word_tokenize
import deplacy
import importlib

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

#Clause segmentation

def spacy_tokenizer(docs, language = 'en', model='en_core_web_sm', token = 'clause',lowercase=False, display_tree = False, remove_punct=True, clause_remove_conj = True, avoid_split_tokenizer=True):
	# TODO: split if you find ";"
	# TODO: make into list comprehensions for faster processing
	if token == 'word':
		# doc = 'I am a boy'
		my_module = importlib.import_module("spacy.lang."+language) # from spacy.lang.en import English
		if language=='en':
			nlp = my_module.English()
			if avoid_split_tokenizer:
				nlp.tokenizer.rules = {key: value for key, value in nlp.tokenizer.rules.items() if "'" not in key and "’" not in key and "‘" not in key}
		tokens_for_all_docs = []
		for doc in docs:
			doc = nlp(doc)
			if lowercase:
				tokens = [token.text.lower() for token in doc]
			else:
				tokens = [token.text for token in doc]
			tokens_for_all_docs.append(tokens)
		return tokens_for_all_docs

	elif token =='clause':
		nlp = spacy.load(model)
		if avoid_split_tokenizer:
			nlp.tokenizer.rules = {key: value for key, value in nlp.tokenizer.rules.items() if "'" not in key and "’" not in key and "‘" not in key}

		chunks_for_all_docs = []
		for doc in nlp.pipe(docs):
			# doc = en(text)
			if display_tree:
				print(doc)
				print(deplacy.render(doc))


			seen = set() # keep track of covered words
			chunks = []
			for sent in doc.sents:
				heads = [cc for cc in sent.root.children if cc.dep_ == 'conj']

				for head in heads:
					words = [ww for ww in head.subtree]
					if remove_punct:
						words = [n for n in words if not n.is_punct]
					for word in words:

						seen.add(word)
					if clause_remove_conj:
						chunk = []
						for i,word in enumerate(words):
							len_minus_1 = len(words)-1
							# print(i, word.tag_, word.text)
							if not (word.tag_=='CC' and i==len_minus_1):
								chunk.append(word)
						chunk = (' '.join([ww.text for ww in chunk]))
					else:
						# dont remove
						chunk = (' '.join([ww.text for ww in words]))
					chunks.append( (head.i, chunk) )

				unseen = [ww for ww in sent if ww not in seen]
				if remove_punct:
					unseen = [n for n in unseen if not n.is_punct]
				if clause_remove_conj:
					chunk = []
					for i,word in enumerate(unseen):
						# print(i, word.tag_, word.text)
						len_minus_1 = len(unseen)-1
						if not (word.tag_=='CC' and i==len_minus_1):
							chunk.append(word)
					chunk = (' '.join([ww.text for ww in chunk]))
				else:
					chunk = ' '.join([ww.text for ww in unseen])
				chunks.append( (sent.root.i, chunk) )

			chunks = sorted(chunks, key=lambda x: x[0])
			chunks = [n[1] for n in chunks]

			if lowercase:
				chunks = [n.lower() for n in chunks]

			chunks_for_all_docs.append(chunks)
		return chunks_for_all_docs
	else:
		raise ValueError("Possible tokens are 'word', 'clause', others are not implemented.")
	
#Verbal tense and aspect detection
#Look into categories and unify them (https://en.wikipedia.org/wiki/Grammatical_aspect#By_language Aspect (!))
nlp = spacy.load('en_core_web_sm')

def detect_aspect(sentences): #Sentences has to be a list of strings (!)
    results = [] #Empty list to save the results 
    for sentence in sentences:
        doc = nlp(sentence)
        tense = None #Empty variables to then determine both tense and aspect
        aspect = None
        #Abbreviations POS (Spacy): https://www.sketchengine.eu/penn-treebank-tagset/
        # Find the tense of the sentence
        for token in doc:
            if token.tag_.startswith('V'):
                if token.tag_ in ['VB', 'VBP', 'VBZ']:
                    tense = 'present'
                elif token.tag_ in ['VBD', 'VBN']:
                    tense = 'past'
                elif token.tag_ in ['VBG']:
                    if 'aux' in [child.dep_ for child in token.children]:
                        aspect = 'continuous'
                    else:
                        tense = 'present'
                elif token.tag_ in ['MD']:
                    aspect = 'modal'
                    if token.lemma_ == 'will' or token.lemma_ == 'shall':
                        if 'VB' in [child.tag_ for child in token.head.children]:
                            tense = 'future'
                            break
        if tense == 'present':
            continuous_flag = False #Using boolean logic to reduce the possibilities of classification
            future_going_flag = False
            for token in doc:
                if token.tag_ == 'VBG' and token.text == 'going':
                    if 'aux' in [child.dep_ for child in token.children]:
                        aspect = 'future_going_to'
                        future_going_flag = True
                    else:
                        aspect = 'going_to'
                        future_going_flag = True
                    break
                elif token.tag_ == 'VBG':
                    if any(tok.dep_ == 'aux' for tok in token.subtree):
                        aspect = 'continuous'
                        continuous_flag = True
                        break

            if not continuous_flag and not future_going_flag:
                for token in doc:
                    if token.tag_ == 'MD' and token.lemma_ in ['will', 'shall']:
                        tense = 'future'
                        aspect = 'simple_future'
                        break

            if aspect is None and tense != 'future':
                aspect = 'simple_present'
        elif tense == 'past':
            if any(token.text == 'had' and token.dep_ == 'aux' for token in doc):
                aspect = 'pluperfect'
            elif any(token.text == 'was' and token.dep_ == 'aux' for token in doc):
                aspect = 'past_continuous'
            elif any(token.text == 'had' and token.dep_ == 'aux' and token.head.tag_ == 'VBN' for token in doc):
                aspect = 'past_perfect'
            else:
                aspect = 'simple_past'
        elif tense == 'future':
            aspect = 'simple_future'
        else:
            aspect = 'simple_present'

        results.append(aspect)

    return results