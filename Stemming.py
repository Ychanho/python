import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

sentence = "Hi . This is Tom . I have many cars ."
sentence = sentence.lower()
tokens = nltk.word_tokenize(sentence)
stop = set(stopwords.words('english'))
tokens = [t for t in tokens if t not in stop]
porter_stemmer = PorterStemmer()
tokens = [porter_stemmer.stem(token) for token in tokens]
print(tokens)

