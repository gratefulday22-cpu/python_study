## 조건에 따라 분기하기 : 조건문
# 조건이 하나일 때 : if문
weather = "비"
if weather == "비":
    print("우산을 챙기세요.")

# 조건이 여러개일 때 : elif문
weather = "맑음"
if weather == "비":
    print("우산을 챙기세요.")

weather = "미세먼지"
if weather == "비":
    print("우산을 챙기세요.")
elif weather == "미세먼지":
    print("마스크를 챙기세요.")

# 모든 조건에 맞지 않을 때 : else문
weather = "맑음"
if weather == "비":
    print("우산을 챙기세요.")
elif weather == "미세먼지":
    print("마스크를 챙기세요.")
else:
    print("준비물이 필요 없어요.")

# input() 함수 사용
weather = input("오늘 날씨는 어때요? ")
print(weather)

weather = input("오늘 날씨는 어때요? ")
if weather == "비":
    print("우산을 챙기세요.")
elif weather == "미세먼지":
    print("마스크를 챙기세요.")
else:
    print("준비물이 필요 없어요.")

# if 문의 조건 변경 (논리 연산자 and, or 사용 가능)
weather = input("오늘 날씨는 어때요? ")

if weather == "비" or weather == "눈" :
    print("우산을 챙기세요.")
elif weather == "미세먼지":
    print("마스크를 챙기세요.")
else :
    print("준비물이 필요 없어요. ")

# 정수형으로 입력 받기 : input()함수는 항상 문자열로 저장하므로, 형변환 필요 

# 풀이1
temp = int(input("오늘 기온은 어때요? "))
if 30<=temp:
    print("너무 더워요, 외출을 자제하세요.")
elif 10<= temp and 30>temp:
    print("활동하기 좋은 날씨예요.")
elif 0<=temp and 10>temp:
    print("외투를 챙기세요.")
else:
    print("너무 추워요. 나가지 마세요.")


#풀이2
temp = int(input("오늘 기온은 어때요? "))
if 30<=temp:
    print("너무 더워요, 외출을 자제하세요.")
elif 10<= temp < 30:
    print("활동하기 좋은 날씨예요.")
elif 0<= temp < 10:
    print("외투를 챙기세요.")
else:
    print("너무 추워요. 나가지 마세요.")

#풀이3
temp = int(input("오늘 기온은 어때요? "))
if 30<=temp:
    print("너무 더워요, 외출을 자제하세요.")
elif 10<= temp:
    print("활동하기 좋은 날씨예요.")
elif 0<= temp :
    print("외투를 챙기세요.")
else:
    print("너무 추워요. 나가지 마세요.")

# 같은 일 반복하기 : 반복문
# for문 : for 변수 in 반복 대상 - 반복 대상에서 하나씩 가져와 변수로 가져오면서 실행
for waiting_no in [1,2,3,4,5]:
    print("대기번호 : {0}".format(waiting_no))


for waiting_no in range(5): #0이상 5미만의 연속한 정수를 for문 안의 변수로 사용
    print("대기번호 : {}".format(waiting_no))

for waiting_no in range(1,6): #1이상 6미만의 연속한 정수를 for문 안의 변수로 사용 
    print("대기번호 : {}".format(waiting_no))

for waiting_no in range(1,6,2): #0이상 5미만의 연속한 정수를 for문 안의 변수로 사용, 간격 2씩
    print("대기번호 : {}".format(waiting_no))


orders = ["아이언맨", "토르", "스파이더맨"]
for customer in orders:
    print("{0}님, 커피가 준비되었습니다. 픽업대로 와 주세요".format(customer))

for customer in ["아이언맨", "토르", "스파이더맨"]:
    print("{0}님, 커피가 준비되었습니다. 픽업대로 와 주세요".format(customer))

# while문 : 조건 만족할 동안 계속 반복
customer = "토르"
index = 5 # 초깃값

while index >=1:
    print("{}님, 커피가 준비되었습니다.".format(customer))
    index = index-1 # while문의 명령 하에 있으므로 계속 1씩 빼면서 반복 실행됨. index -=1 로 써도 동일
    print("{}번 남았어요.".format(index))
    if index == 0:
        print("커피를 폐기 처분합니다.")

# while문 코드에 탈출 구문이 없으면, 무한 반복 실행 (Ctrl C : 강제 종료)
customer = "아이언맨"
index = 1
while True :
    print("{}님, 커피가 준비되었습니다. 호출{}회".format(customer,index))
    index = index + 1 #index +=1 로 써도 동일

# input() 함수로 값 입력받아 while문 실행하기
customer = "토르"
person = None

while person !=customer:
    print("{}님, 커피가 준비되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요? ")


# 반복문의 흐름 제어하기 : continue와 break
# continue : 건너뛰기 
absent = [2,5]
for student in range(1,11):
    if student in absent:
        continue
    print("{}번 학생, 책을 읽어 보세요".format(student))

#break : 반복문 탈출
absent = [2,5]
no_book = [7]
for student in range(1,11):
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업은 여기까지, {}번 학생은 교무실로 따라와요".format(student))
        break
    print("{}번 학생, 책을 읽어 보세요".format(student))

# for문 한 줄로 작성하기 : 리스트 컴프리헨션 - 동작 for 변수 in 반복 대상
# 예제1 : 리스트에서 100씩 더하기 
students = [1,2,3,4,5]
print(students)

students = [i + 100 for i in students] #i는 임의로 사용한 변수명이므로 바꿔도 됨. 
print(students)

# 예제2 : 리스트 글자수 담은 정보로 변형하기 
students = ["Iron man", "Thor", "Spider Man"]
students = [len(i) for i in students]
print(students)


# 예제3 : 리스트 전부 대문자로 바꾸기 
students = ["Iron man", "Thor", "Spider Man"]
students = [i.upper() for i in students] #리스트 컴프리헨션으로 만든 리스트를 새롭게 저장
print(students)

## 실습 문제 : 택시 승객 수 구하기 


headcount = 0

for customer in range(1,51):
    
    from random import *
    time = randint(5,50)

    if 5<= time <=15:
        headcount += 1 
        print("[0]"+ "{}번째 손님".format(customer) + " (소요시간 :"+str(time)+"분)")

    else:
        print("[]"+ "{}번째 손님".format(customer)+ " (소요시간 :" +str(time)+"분)")

print("총 탑승객 : {}명".format(headcount))



## 실습문제 해설
from random import *

headcount = 0
for customer in range (1,51):
    time = randrange(5,51)
    if 5 <= time <= 15:
        print("[0] {}번째 손님 (소요시간 : {}분)".format(customer,time))
        headcount = headcount + 1 #headcount += 1 도 가능
    else:
        print("[] {}번째 손님 (소요시간 : {}분)". format(customer, time))

print("총 탑승객 : {}명".format(headcount))   

## 셀프체크 : 가격 계산 프로그램 작성

from random import * 
num = randrange(3,100,3)

for i in range(num):
    print("2+1 상품입니다.")

price = (num-1)*1000 
print("총 가격은 {}원입니다".format(price))

## 셀프체크 해설
price = 1000 # 개당 가격
goods = 3 # 상품 구매 갯수
total = 0 # 총 가격

for i in range (1, goods+1): # 1부터 goods + 1의 범위까지 반복 (현재 goods 의 초깃값이 3이므로 1~4미만 반복
    print("2+1 상품입니다.")
    if i%3 == 0 : #3의 배수이면
        continue # continue 아래 있는 반복문은 건너뜀. 
    total = total + price

print("총 가격은 " + str(total) + "원입니다.")