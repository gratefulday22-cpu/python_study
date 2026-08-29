#리스트 : 서로 연관된 값들을 묶어서 관리하기 위한 기능 

subway=[10,20,30] #각 값의 자료형은 달라도 Ok
print(subway)
empty_list = []

subway=["푸","피글렛","티거"] #문자열도 저장 가능
print(subway)
print(subway.index("피글렛")) #리스트에서도 인덱스가 있음. 역시 0부터 시작

subway.append("이요르") #리스트 끝에 값 추가하기 : 리스트명.append(추가할 값)
print(subway)

subway.insert(1, "루") #리스트 중간에 값 삽입하기 : 리스트명.insert(인덱스, 추가할 값)
print(subway)

print(subway.pop()) #리스트에서 값 삭제하기 (끝에서부터 하나씩 삭제 후 저장) : 리스트명.pop()
print(subway) 
print(subway.pop()) 
print(subway)
print(subway.pop()) 
print(subway)

subway.clear() #리스트에서 값 한 번에 삭제하기 : 리스트명.clear() 
print(subway)

#중복 값 확인하기 : 리스트명. count()
subway=["푸","피글렛","티거"]
subway.append("푸")
print(subway)

print(subway.count("푸"))

#리스트 정렬하기 : 리스트명.sort() - 오름차순 정렬 
num_list=[5,2,4,3,1]
print(num_list.sort()) # sort(_함수는 오름차순 정렬만 하고, 값을 반환하는 함수가 아니어서 print()안에 바로 넣으면 None이 나옴

num_list=[5,2,4,3,1]
num_list.sort() # 요렇게 두 줄에 걸쳐서 먼저 정렬을 하고, 
print(num_list) # 그 변경된 (정렬된) 값을 출력


## GPT 코멘트 
# ① 원본(변수, 문자열)은 그대로 두고 새로운 값을 반환하는 함수/메서드
# len(), str(), upper() 등 > 새로운 값을 생성하는 것이므로 print()안에 바로 넣어도 결과 나옴 

# ② 원본 객체 자체를 변경하고, None을 반환하는 함수/메서드 
# sort(), reverse() 등 

#리스트 정렬하기 : 리스트명.sort(reverse=True) - 내림차순 정렬 
num_list=[5,2,4,3,1]
num_list.sort(reverse=True) #반대로 정렬할까요? = 네
print(num_list) 

#정렬 순서 변경 : 리스트명.reverse()
num_list=[5,2,4,3,1]
num_list.sort(reverse=True) #반대로 정렬할까요? = 네
print(num_list) 
num_list.reverse()
print(num_list)

# 정렬하면서 새로운 값을 반환하려면 : sorted(리스트명)
my_list=[1,3,2]
my_list.sort() #my_list 자체를 오름차순 정렬하여 변경 
print(my_list)

my_list=[1,3,2]
new_list=sorted(my_list) #리스트명.sorted() 가 아니라, sorted(리스트명) 으로 호출함에 주의
print(new_list)

my_list=[1,3,2]
print(sorted(my_list))

## GPT 코멘트 : 함수와 메서드의 호출 방식 차이
# 함수 : 함수 (대상) - 독립적으로 존재하는 기능, 함수 자체는 독립 기능으로 있고, 거기에 대상을 가져다놓는 느낌 (기능 중심)
# 메서드 : 대상.메서드명() - 특정 객체에 딸려 있는 기능 - 이 대상에 대해 어떠한 메서드를 실행해라는 느낌 (대상 중심)

# 리스트 확장하기 : 리스트 안에는 여러 자료형 섞어서 넣어도 됨, 문자열 넣어도 됨, 또다른 리스트 넣어도 됨 
mix_list = ["푸", 20, True, [5,2,4,3,1]]
print(mix_list)

# 서로 다른 리스트 합치기 : 리스트명1.extend(리스트명2)
mix_list=["푸",20,True]
num_list=[5,2,4,3,1]
mix_list.extend(num_list)
print(mix_list) #합쳐진 결과는 리스트 1에 저장됨 ! 즉 extend() 앞에 쓴 리스트 기준으로 저장
print(num_list)


## 딕셔너리 : key와 Value의 일대일 대응(:) 관계 (key는 중복 허용 x, 변경되지 않는 값으로)
cabinet = {3:"푸", 100:"피글렛"}
empty_dict={} #빈 딕셔너리도 생성 가능

#딕셔너리 value에 접근하는 방법 : 딕셔너리에서는 key가 인덱스 역할 
print(cabinet[3]) # 방법1: 딕셔너리명[key] - 정의되지 않은 key 전달 시 오류 발생, 프로그램 종료 
print(cabinet[100])
print(cabinet[5]) # 오류 발생, 프로그램 종료 
print("hi")

#방법2: 딕셔너리명.get(key, 디폴트값) value가 없는 key 에 접근 시 디폴트값인 None 반환, 프로그램 계속 / 디폴트값은 설정 가능
print(cabinet.get(100))
print(cabinet.get(5)) # None 반환
print("hi")
print(cabinet.get(5,"사용 가능")) # 디폴트값으로 두 번째 인자를 반환하도록 설정 가능

# in함수 : 딕셔너리 안에 특정 key가 있는지 없는지 확인 -> 있으면 True, 없으면 False 반환
print(3 in cabinet)
print(5 in cabinet)

# 딕셔너리의 key에는 문자열도 넣을 수 있음. 접근할 때도 ""로 감싸서 문자열로 호출해야.
cabinet = {"A-3" : "푸", "B-100" : "피글렛"}
print(cabinet["A-3"])
print(cabinet["B-100"])
print(cabinet["C-14"]) # 오류 발생 후 프로그램 종료됨
print("hi")

print(cabinet.get("A-3"))
print(cabinet.get("B-100"))
print(cabinet.get("C-14", "이용 가능"))
print("hi")

# in은 문자열 안에 특정 문자가 포함되었는지 확인할 때도 사용 가능
print("곰" in "곰돌이")
print("댕" in "댕댕이")
print("푸" in "곰돌이")

# 딕셔너리에 key 있으면 변경, 없으면 key:value 쌍으로 추가하기 : 딕셔너리명[key] = 변경 또는 추가할 value
cabinet = {"A-3" : "푸", "B-100" : "피글렛"}
print(cabinet)
cabinet["A-3"] = "티거"
cabinet["C-20"] = "이요르"
print(cabinet)

# 딕셔너리에서 key 삭제하기 : del 딕셔너리명 [key]
cabinet = {"A-3" : "푸", "B-100" : "피글렛"}
print(cabinet)
del cabinet ["A-3"] 
print(cabinet)

# 딕셔너리에 남아있는 key만 출력 : 딕셔너리명.keys()
cabinet = {"A-3" : "푸", "B-100" : "피글렛", "C-20" : "이요르"}
print(cabinet.keys())

# 딕셔너리에 남아있는 value만 출력 : 딕셔너리명.values()
cabinet = {"A-3" : "푸", "B-100" : "피글렛", "C-20" : "이요르"}
print(cabinet.values())

# 딕셔너리에 남아있는 key : value 함께 출력 : 딕셔너리명.items()
cabinet = {"A-3" : "푸", "B-100" : "피글렛", "C-20" : "이요르"}
print(cabinet.items())

# 딕셔너리에 있는 값 모두 한 번에 삭제 : 딕셔너리명. clear()
cabinet = {"A-3" : "푸", "B-100" : "피글렛", "C-20" : "이요르"}
cabinet.clear() #clear는 값을 반환하는 함수가 아니므로 print()에 바로 넣지 말고 따로 실행 후 결과를 넣기 
print(cabinet)

## 튜플 : 읽기 전용 리스트, 소괄호로 정의, 최초 정의 이후 값의 수정이나 삭제 불가능
menu = ("돈가스", "치즈돈가스")
print(menu[0]) #튜플명[인덱스] 로 접근 
print(menu[1])

name = "피글렛"
age = 20
hobby = "코딩"
print(name,age,hobby)

# 튜플 형태로 인덱스 매겨서 한 번에 여러 변수 정의 가능 / 인덱스로 순서가 있으므로, 슬라이싱도 가능 
(name, age, hobby) = ("피글렛", 20, "코딩")
print(name,age,hobby)

(departure, arrival) = ("김포", "제주")
print(departure, ">", arrival)
(departure, arrival) = (arrival, departure)
print(departure, ">", arrival)

## 세트 (집합) : 중괄호로 정의, 순서 x 중복 x
my_set = {1,2,3,3,3}
print(my_set)

# 세트에 값을 지정하는 두 가지 방법 (정수, 문자열 등 다양한 형태의 자료형 값으로 지정 가능)
# 방법1 : 세트명 = {값1,값2,값3}
java = {"푸", "피글렛", "티거"}
# 방법2 : 세트명 = set([값1,값2,값3])
python = set(["푸", "이요르"])

empty_set = set([])

# 서로 다른 세트에서 교집합 출력 : 세트명1 & 세트명2 또는 세트명1.intersection(세트명2)
java = {"푸", "피글렛", "티거"}
python = {"푸", "이요르"}
print(java & python)

java = set(["푸", "피글렛", "티거"])
python = set(["푸", "이요르"])
print(java.intersection(python))

# 서로 다른 세트에서 합집합 출력 : 세트명1 | 세트명2 또는 세트명1.union(세트명2)
java = {"푸", "피글렛", "티거"}
python = {"푸", "이요르"}
print(java|python) # 중복 제외하고 출력
java = {"푸", "피글렛", "티거"}
python = {"푸", "이요르"}
print(java.union(python)) # 순서 보장하지 않으므로, 출력할 때마다 순서는 달라짐 (인덱스가 없음)

# 서로 다른 세트에서 차집합 출력 : 세트명1 - 세트명2 또는 세트명1.difference(세트명2)
java = {"푸", "피글렛", "티거"}
python = {"푸", "이요르"}
print(java-python)
print(java.difference(python))

# 집합에 값 추가 : 집합명.add(값)
python.add("피글렛")
print(python)

# 집합에서 값 삭제 : 집합명.remove(값)
java.remove("피글렛")
print(java)

## 자료구조 간 변환 : 바꾸고 싶은 자료구조로 현재의 자료구조 다시 감싸주면 됨 
menu = {"커피", "우유", "주스"}
print(menu)
print(type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu,type(menu))

menu = set(menu)
print(menu, type(menu))

## 세트로 형변환해서 중복이 제거될 경우, 중복 제거 상태가 계속 유지됨. 즉 리스트 -> 세트 -> 리스트 로 다시 돌려도 중복값이 부활하는 것 아님
my_list = [1,2,3,3,3]
print(my_list,type(my_list))

my_set = set(my_list)
print(my_set, type(my_set)) # 세트로 변환하여 중복 제거 

my_list = list(my_set)
print(my_list, type(my_list)) # 다시 형변환하여 리스트가 되었으나, 중복은 제거됨 다시 [1,2,3,3,3]으로 돌아오는거 아님

## 실습 문제 : 당첨자 뽑는 추첨 프로그램 작성
from random import *
my_list = [1,2,3,3,5]
print(my_list)
shuffle(my_list)
print(my_list)
print(sample(my_list,2))
my_set = set(my_list)
print(my_set, type(my_set))
my_list=list(my_set)
print(sample(my_list,2))

# 풀이
from random import *
users = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print("--당첨자 발표--")
print("치킨 당첨자 : " + str(sample(users,1)))
print("커피 당첨자 : " + str(sample(users,3)))
print("--축하합니다!--")

# 답
from random import *
users = range(1,21) 
users = list(users)
shuffle(users)

winners = sample(users, 4)
print("--당첨자 발표--")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("--축하합니다!--")

## 셀프체크
# 풀이 
subjects = ["자료구조", "알고리즘", "자료구조", "운영체제"]
print(subjects)
subjects = set(subjects)
print(subjects, type(subjects))
subjects=list(subjects)
print(subjects,type(subjects))

print("신청한 과목은 다음과 같습니다.")
print(subjects)



