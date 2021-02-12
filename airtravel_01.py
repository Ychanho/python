class Flight:
    # pass # 아무것도 아닌 것
    # def number(self):
    #     return 'KE081'

    # #--------------------------------
    # def __init__(self):
    #     print('init')
    #     super().__init__()
    # def __new__(cls):
    #     print('new')
    #     return super().__new__(cls)
    # def number(self):
    #     return  'KE081'

#---------------------------------------
    # def __init__(self, number):
    #     self._number = number
    #
    # def number(self): #메소드 작성
    #     return  self._number


#-----------------------------------------
#유효성 검사


#-----------------------------------------
    #변수 추가
    def __init__(self, number, passenger_num):
        self._number = number
        self._passenger_num = passenger_num

    def number(self): #메소드 작성
        return  self._number

    def add_passenger(self,num):
        self._passenger_num += num