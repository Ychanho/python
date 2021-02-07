import re #이걸 먼저 선언해줘야 line8의 특수문자 제거가 문제없이 기능한다.
text = "Apple is fruit. Orange is also fruit. Tomato is Fruit?"

def word_index_count(text):
    word_id = []
    id_frequency = {}
    text = text.lower()  #소문자로 변환
    text = re.sub('[.,!?"\';~()`]', '', text) # , 다음에 한칸 띄워줘야 함
    word_list = text.split(" ") #" "사이의 문자를 기준으로 나눠서 리스트에 담음
    for word in word_list: #list에서 순서대로 단어를 가져와서 word_id에 있으면 id_frequency의 j번째 성분의 카운팅을 1올리고 word_id에 없으면 word_id에 그 단어를 추가하고  id_frequency의j번째 성분에 1을 부여하려고 했음
        for j, word2 in enumerate(word_id):
            if word == word2:
                id_frequency[j] = id_frequency[j] + 1
            else:
                word_id.append(word)
                id_frequency[j] = 1

    return word_id, id_frequency

print(word_index_count(text))
# 왜 worf_id와 id_frequency가 갱신되지 않을까
#--------------------------  word_id는 단어 리스트만 id_frequency는 횟수 리스트만 들어가는 줄 착각했었음

def word_index_count(text):
    word_id = {}
    id_frequency = {}
    text = text.lower()  # 소문자로 변환
    text = re.sub('[.,!?"\';~()`]', '', text)  # , 다음에 한칸 띄워줘야 함
    word_list = text.split(" ")
    j=0  #j로 카운팅하는게 최적화된 방법일까?
    for i, word in enumerate(word_list):
        if word in word_id:
            id_frequency[word_id[word]] += 1
        else:
            word_id[word] = j
            id_frequency[j] = 1
            j = j + 1

    return word_id, id_frequency

print(word_index_count(text))



