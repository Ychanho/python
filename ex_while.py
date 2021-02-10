# 1
# while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구하세요.
n = 1
sum = 0
while n <= 1000:
    if n % 3 == 0:
        sum = sum + n
        n += 1
    else:
        sum = sum
        n += 1
        # n에 1더하는걸  if 와 else 일 때 둘다 적어 주는 거 말고 방법이 없나
print(sum)


#2 While 문을 사용해 *들을 출력
# n = 1
# while n < 6:
#     print('*'*n) # 다음 회차에서 알아서 다음줄로 프린트 된다.
#     n = n+1

# #3 리스트 내포를 이용해 한 줄로 구현해보세요.
# numbers = [1, 2, 3, 4, 5]
# result = [n+2 for n in numbers if n%2 ==0 ] #뒤에 : 안 붙여도 됨
# print(result)