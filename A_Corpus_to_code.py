#Try another logic, a boolean one. Using POS to track if it could be a match.
import nltk

#General function to track it

def has_syntax(text, syntax):
    
    tokens = nltk.word_tokenize(text)
    pos_tags = nltk.pos_tag(tokens)
    tags = [tag for _, tag in pos_tags]
    tags_str = " ".join(tags)
    return syntax in tags_str

#Trying a simple structure of SITB Current (High risk):
#The original sentence was 'I just want to die'. This is a variation and it worked.

text = "I just want to kill myself" #Following sentence 'I'm close to suicide'? Might be recurrent
syntax = "PRP RB VBP TO VB"
result = has_syntax(text, syntax)
print(f"The sentence '{text}' shows a high risk structure: {result}")

#Trying a simple structure of SITB Past (Medium risk?):
#The original sentence was Last night I tried to kill myself. I try a similar variation and it worked

text = "Last week I tried to kill myself" 
syntax = "JJ NN PRP VBD TO VB PRP"
result = has_syntax(text, syntax)
print(f"The sentence '{text}' shows a medium risk structure: {result}")

#Trying a simple structure of SITB Future (Medium/high risk?):

text = "I will kill myself" 
syntax = "PRP MD VB PRP"
result = has_syntax(text, syntax)
print(f"The sentence '{text}' shows a medium/high risk structure: {result}")



