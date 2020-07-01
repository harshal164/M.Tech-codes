from nltk.tokenize import sent_tokenize ,word_tokenize

text = 'Hello everyone. "Welcome to GeeksforGeeks". You are studying NLP article'
print(sent_tokenize(text) )

import nltk.data 

# Loading PunktSentenceTokenizer using English pickle file 
tokenizer = nltk.data.load('tokenizers/punkt/PY3/english.pickle') 

print(tokenizer.tokenize(text) )
print(word_tokenize(text))