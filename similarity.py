import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import numpy as np

doc1 = 'Rafael Nadal Parera is tennis player.'
doc2 = 'Donald Trump is president.'
doc3 = 'Donald Trump has yellow hair.'

doc1 = doc1.lower()
doc2 = doc2.lower()
doc3 = doc3.lower()

# tokenize
tokens1 = nltk.word_tokenize(doc1)
tokens2 = nltk.word_tokenize(doc2)
tokens3 = nltk.word_tokenize(doc3)

#stopword 제거
stop = set(stopwords.words('english'))
tokens1 = [t for t in tokens1 if t not in stop]
tokens2 = [t for t in tokens2 if t not in stop]
tokens3 = [t for t in tokens3 if t not in stop]

#stemming
porter_stemmer = PorterStemmer()
tokens1 = [porter_stemmer.stem(token) for token in tokens1]
tokens2 = [porter_stemmer.stem(token) for token in tokens2]
tokens3 = [porter_stemmer.stem(token) for token in tokens3]

print(tokens1)
print(tokens2)
print(tokens3)

# Doc-word matrix
doc_word = tokens1 + [t for t in tokens2 if t not in tokens1]
doc_word = doc_word + [t for t in tokens3 if t not in doc_word] # 36~37행을 한 줄로 표현 가능할까?
# doc_word = list(set(tokens1 + tokens2 + tokens3)) # 36~37행을 한 줄로 하면 이렇게
print(doc_word)



OHtoken1 = [1 if doc_word[j] in tokens1 else 0 for j in range(len(doc_word))]
OHtoken2 = [1 if doc_word[j] in tokens2 else 0 for j in range(len(doc_word))]
OHtoken3 = [1 if doc_word[j] in tokens3 else 0 for j in range(len(doc_word))]
# for j in len(doc_word)가 아니라
# for j in range(len(doc_word)) range 안 붙이면 TypeError: 'int' object is not iterable
OHtoken1 = np.array(OHtoken1)
OHtoken2 = np.array(OHtoken2)
OHtoken3 = np.array(OHtoken3)
print(OHtoken1)
print(OHtoken2)
print(OHtoken3)


#Cosine similarity 정의
def get_sim(A, B):
    s1 = np.dot(A, B)
    s2 = np.sqrt(np.sum(A*A))
    s3 = np.sqrt(np.sum(B*B))
    return s1 / (s2*s3)

# Similarity 구하기
print('doc1 & doc2: ', get_sim(OHtoken1, OHtoken2))
print('doc1 & doc3: ', get_sim(OHtoken1, OHtoken3))
print('doc2 & doc3: ', get_sim(OHtoken2, OHtoken3))