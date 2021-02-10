f = open("./fileIO.txt", 'r', encoding='utf-8')
lines = f.readlines()
name_age ={}

#파일 구성이 어떻게 돼 있나 보기
print(lines)
#성과 나이를 딕셔너리로 할당하기
for line in lines:
    word = line.split()
    name_age[word[0]] = word[1]

print(name_age)