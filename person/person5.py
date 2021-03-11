# 추상 클래스

from abc import *       # import *가 있으면 abc의 모든 것을 import 하겠다는 의미
# 실제로 쓸 때는 필요 없는 것까지 가져오기 때문에 필요한 것들 일일이 import를 함

class StudentBase(metaclass=ABCMeta):
    @abstractmethod
    def study(self):
        pass
    @abstractmethod
    def go_to_school(self):
        pass

class Student(StudentBase):
    def study(self):
        print('학생은 공부를 해야합니다.')
    def go_to_school(self):
        print('학생은 학교를 가야합니다.')