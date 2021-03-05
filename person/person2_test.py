# 1 자식 클래스에 __init__ O
from lecture_6.python.person2 import Student

kim = Student(2)
print(kim.num_arm)
print(kim.semester)

# # 2 자식 클래스에 __init__ X
# from lecture_6.python.person2 import Student
#
# kim = Student()
# print(kim.num_arm)
