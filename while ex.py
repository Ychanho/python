# 단순 while문
prompt = """
1. Add
2. Del
3. Quit"""
number = 0
while number != 3:
    print(prompt)
    number = int(input("Enter number:"))

# # break문
# coffee = 3
# while True:
#     money = int(input("돈을 넣어주세요.:"))
#     if money == 300:
#         print("맛있게 드세요.")
#         coffee = coffee - 1
#     elif money > 300:
#         print(f'거스름돈은 {money - 300}원입니다.')
#         print("맛있게 드세요.")
#         coffee -= 1     # coffee = coffee - 1와 같은 의미
#     else:
#         print(f'{300 - money} 더 넣어주세요.')
#     if coffee == 0:
#         print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
#         break


# # continue
# coffee = 3
# while coffee > 0:
#     print(f'남은 거피: {coffee}')
#     money = int(input("돈을 넣어 주세요: "))
#     if money < 300:
#         continue
#     coffee -= 1
#     print("맛있게 드세요")