# #function사용법
# #1
# def sum(a,b):
#     s = a+b #변수제목은 임의로 지정
#     return s
# #2
# def sum(a,b):
#     return a+b  #1과 같은 결과

# print(sum(3,5))
# print(sum(2,1))

#3
def sum_and_mul(a, b): #뒤에 :적어야 함
    return a*b, a+b

s, m =sum_and_mul(3,5)
print(s)
print(m)
print(sum_and_mul(3,5))
print(sum_and_mul(2,1))