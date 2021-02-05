#1
marks = [90, 25, 67, 45, 80, 75, 82]
number = 0
for mark in marks: #enumerate를 사용해서 똑같이 할 수 있다
    number = number +1
    if mark >= 60:
        print("%d번 학생은 합격" %number)
    else:
        print("%d번 학생은 불합격" %number)
#
# #1-2
# marks = [90, 25, 67, 45, 80, 75, 82]
#
# for i, mark in enumerate(marks):
#     i=i+1
#     if mark >= 60:
#         print("%d번 학생은 합격" %(i))
#     else:
#         print("%d번 학생은 불합격" %(i))

# #2
# marks = [90, 25, 67, 45, 80, 75, 82]
# number = 0
#
# for mark in marks:
#     number = number +1
#     if mark < 60:
#         print("%d번 학생 기준미달입니다"%number)
#     elif mark <80:
#         continue #if문이 맞을 때 그냥 넘어감
#
#     print("%d번 학생 축하합니다. 합격입니다." %number)

# #3
# for i in range(10):
#     print(i)
#
# #4
# sum =0
# for i in range(1,11):#1부터 11미만 즉 1부터 10까지
#     sum +=  i
#     print(sum)

#5 구구단 출력
# for i in range(2,10):#2부터 9
#     for j in range(1, 10):
#         print(i*j, end=" ")
#     print('')
#
# #6
# numbers = [1,2,3,4,5]
# result = []
# for n in numbers:
#     if n%2 ==1:
#         result.append(n*2) #append는 기존 리스트에 추가하는 것
# print(result)