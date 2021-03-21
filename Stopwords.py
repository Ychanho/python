import nltk
from nltk.corpus import stopwords

sentence = "Hi . This is Tom . I have many cars ."
sentence = sentence.lower()
tokens = nltk.word_tokenize(sentence)
stop = set(stopwords.words('english'))
tokens = [t for t in tokens if t not in stop]
print(tokens)
print('this' in stop)