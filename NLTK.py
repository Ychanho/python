import nltk

# nltk.download()

sentence = "Hi . This is Tom . I have many cars ."
sentence = sentence.lower()
tokens = nltk.word_tokenize(sentence)
print(tokens)
text = nltk.Text(tokens)
print(text)
print(len(text.tokens))
print(len(set(text.tokens)))

for tokens in text.vocab():
    print(tokens, text.vocab()[tokens])

text.plot(5)

text.count('.')
text.count('many')
text.dispersion_plot(['.', 'many']) # 인덱스 0번부터 세는거 잊지말기

