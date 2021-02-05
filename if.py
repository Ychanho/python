#1
man = True
if man :
    print("남자화장실로 가세요")
else:
    print("여자화장실로 가세요")

#2
minimum = 165
height =165

if height < minimum:
    print("탑승할 수 없습니다")
else:
    print("탑승하세요")

# #3
# blood_type = "A"
# emergency_patient = "A"
#
# if blood_type == emergency_patient
#     print("수혈해 주세요")
# else:
#     print("수혈할 수 없습니다")

#4
min = 165 #최소키
max = 195 #최대키
height = 200
if height < min or height > max :
    print("탑승하실 수 없습니다")
else:
    print("탑승하세요")

#5
blood_type1 = "B"
emergency_patient_type1 = "B"
blood_type2 = "RH+"
emergency_patient_type2 = "RH+"

if blood_type1 == emergency_patient_type1 and blood_type2 ==emergency_patient_type2 :
    print("수혈해주세요")
else:
    print("수혈해주실 수 없습니다")

#6
basic = 40
intermediate = 70
advanced =100
score = 80

if score <= basic:
    print("초급반을 수강하세요")
elif score <= intermediate:
    print("중급반을 수강하세요")
elif score <= advanced:
    print("고급반을 수강하세요")
else:
    print("점수를 확인해주세요요")

