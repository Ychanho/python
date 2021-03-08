# 다중 상속 : 여러 부모 클래스로부터 상속 받는 것
class Person:
    def __init__(self):
        self.num_arm = 2
        print("Person class init")

    def greeting(self):
        print('p)안녕하세요')

class University:
    def credit_show(self):
        print("U)학점은 A입니다.")

class Student(Person, University):
    def __init__(self, semester):
        super().__init__()
        print("Student class init")
        self.semester = semester

    def study(self):
        print("공부하기")

    def greeting(self):
        super().greeting()      # 부모 클래스의 greeting을 불러주고 다음줄을 쭉 실행
        print(f's)대학교 {self.semester}학기생입니다.')