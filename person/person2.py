# 1 자식 클래스에 __init__이 들어가 있는 경우 super().__init__()

class Person:           # 부모 클래스
    def __init__(self):
        self.num_arm = 2
        print("Person_init")

class Student(Person):  # 자식 클래스
    def __init__(self, semester):
        super().__init__() # 자식 클래스에 __init__이 들어간다면 super().__init__() 이걸 해줘야 함 그래야 self. 변수들이 실행됨
        print("Studen_init")
        self.semester = semester


# # 2 자식 클래스에 __init__이 안 들어가 있는 경우
#
# class Person:           # 부모 클래스
#     def __init__(self):
#         self.num_arm = 2
#         print("Person_init")
#
# class Student(Person):  # 자식 클래스
#     pass                # 자식 클래스에 __init__이 없다면 super().__init__() 안 해줘도 됨