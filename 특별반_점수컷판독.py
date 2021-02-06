student2score = {
    "Darius": 100,
    "Dr.Mundo": 80,
    "Morgana": 60,
    "Sivir": 75,
    "Yummi": 20,
    "Viktor" : 97
}

def get_special_students(student2score): #맨 뒤에 : 써야 함
    # """
    #
    # :param student2score:
    # :return:
    # """               #""""""을 치니까 알아서 이렇게 되던데 뭐지

    special_students = {}
    for student in student2score.keys():  #맨 뒤에 : 써야 함
        if student2score[student] >= 80:  #맨 뒤에 : 써야 함
           special_students[student] = student2score[student]  #["student"]라 하면 student에 할당된 값이 계속 덮어씌워짐 [student]로 해야 함
           # special_students.append 식으로는 못 하나?
    return special_students

#-------------------------------------------------------------------
# 누가 특별반인가 출력해서 확인
special_students = get_special_students(student2score)
print("특별반에 들어가게 될 학생은")
for name in special_students.keys():
    print(name, special_students[name])

