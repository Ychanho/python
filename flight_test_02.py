from lecture_4.python.airtravel_01 import Flight
f = Flight('KE083', 0)  #airtravel_01 의  def __init__(self, number): 에서 number에 'KE081'이 할당 된 것
f1 = Flight('KE081', 10)
f.add_passenger(2)
f1.add_passenger(3)
f.add_passenger(10)

print(f.number())
print(f._passenger_num)
print(f1._passenger_num)