# #1
# name_to_age = {"Jenny": 20, "Ella":31} # 중괄호를 씀 jenny, ella는 key 20,31은 value
# name_to_age["John"] =26
# name_to_age["Tom"] =41
# print(name_to_age["Jenny"])
# print(name_to_age["John"])
# print(name_to_age.get("Tom"))  #["Tom"]가 아니라 ("Tom")이다
#2
name_to_age = {} # #1같은 과정이다
name_to_age["John"] =26
name_to_age["Tom"] =41

name_to_age["Jenny"]=21
# print(name_to_age["Jenny"])
# print(name_to_age.get("jenny"))
# print(name_to_age.keys())

#
for name in name_to_age.keys():
    print(name, name_to_age[name])
# #
# for i, name in enumerate(name_to_age.keys()):
#     print(i, name, name_to_age[name])
# #
# print("Andrew" in name_to_age)
# print("Ella" in name_to_age)
