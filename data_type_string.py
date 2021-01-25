# print("Hello World")
# print('Hello World')
# print("a")
# print('123', end="a")
# print('456')
#
# c = "Tom's paper"
# print(c)
# d = 'He said "Hi"'
# print(d)
# c ='Tom\'s paper'
# print(c)
# d = "He said \"Hi\""
# print(d)
#
# multiline ="""
# \"\"\" \"\"\" 이 사이에 들어가는 것은 쓰는 대로 출력할 수 있음
# """
# print(multiline)

# teacher = "Kwon's"
# title = "Al School"
# print(teacher+title)
# print("="*30)
#
# print(len(title))
#
# print(title[0])
# print(title[-1])
# print(title[:2])
# print(title[3:])

# odd_even = "홀짝홀짝홀짝"
# print(odd_even[::2])
# print(odd_even[1::2])
# print(odd_even[1:4:2])

# a = 'apple'
# print(a.count("p"))
# print(a.find("p")) #0~n번째 중에 몇번째에 있는지 알려줌
# print(a.index("p")) #0~n번째 중에 몇번째에 있는지 알려줌
# print(".".join(a))
# A=a.upper()
# print(A)
# print(A.lower())


#문자열 포매팅

apple_num =4
orange_num =2
apple_num_string ="three"

print("I eat %d apples." %apple_num)
print("I eat {0} apples.".format(apple_num))
print("I eat %s apples." %apple_num_string)
print("I eat %d apples and %d oranges." %(apple_num, orange_num))
print("I eat {0} apples and {1} oranges.".format(apple_num, orange_num))
print("I eat {apple_num} apples and {orange_num} oranges." .format(apple_num=1, orange_num=2))

print("Erroe is %d%%" %98)
print(f'I eat {apple_num}apples.')
pi =3.141592
print("pi =%f" %pi)
print("pi=%0.4f" %pi)