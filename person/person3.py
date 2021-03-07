# 메소드 오버라이딩
class Person:
    def __init__(self):
        self.num_arm = 2
        print("Person class init")

    def greeting(self):
        print('p)안녕하세요')

class Student(Person):
    def __init__(self, semester):
        super().__init__()
        print("Student class init")
        self.semester = semester

    def study(self):
        print("공부하기")

    def greeting(self):
        super().greeting()      # 부모 클래스의 greeting을 불러주고 다음줄을 쭉 실행
        print(f's)대학교 {self.semester}학기생입니다.')