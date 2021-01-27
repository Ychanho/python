#리스트 예제
#1
language1 = ["C", "C+", "JAVA"]
language2 = ["Python", "Go", "C#"]

#1-1
languages = language1
languages.append(language2[0])
languages.append(language2[1])
languages.append(language2[2])
print(languages)

#1-2
#language1.append(language2) language2의 원소들이 하나의 원소로 합쳐져서 안됨 2의 원소를 일일이 불러다가 하나하나씩 더해야하나?
lan = language1 + language2
print(lan)  # 그냥 합쳐버리면 됨


#2 @@@
nums = [12, 245, 33, 77, 858]
sum = sum(nums[:])
# Q. nums의 마지막 원소는 858이니 0부터 셌을 때 4니 sum(nums[0:4])이 맞지 않나?
# 콜론 기준으로 왼쪽 '이상' 오른쪽 '미만' 이므로, [-4:-1]으로 적는 경우 가장 오른쪽 문자가 출력되지 않음. (#2 문제도 마찬가지로 [0:4]로 쓰면 마지막 원소가 제외됨)
average = sum/len(nums)
print(average)

#3
a = ["b", "a", "d", "c"]
a.sort()
# Q. b = a.sort() 오류가 나는데 a는 기존대로 놔두고 a를 sort한 행렬을 b로 지정하고 싶으면 b=a 로 한 뒤에 b.sort를 해야만 하는가?
# A. b = sorted(a) 와 같은 형태로 사용하면 의도한대로 결과를 출력할 수 있음.
print(a)