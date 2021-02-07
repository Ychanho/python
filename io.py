f = open("./write.txt", 'w', encoding='utf-8') #./ 는 현재 실행중인 파이썬 스크립트의 경로를 의미
f.write("file write")
f.close()

f=open()

# with open

########################################################333

f = open("./write.txt", 'a', encoding='utf-8')
for i in range(10, 20):
    data = f'line{i}\n'
    f.write(data)
f.close()

########################################################333

f = open("./write.txt", 'r', encoding='utf-8')
line = f.readline()
print(line)
f.close()

f = open("./write.txt", 'r', encoding='utf-8')
lines = f.readlines()
for line in lines:
    print(line)
f.close()