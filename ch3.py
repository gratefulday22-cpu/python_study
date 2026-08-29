# 산술 연산자 
print(3+5)
print(5-4)
print(6*8)
print(int(20/5))
print(20//5) # 정수/정수 = 정수로 출력하고 싶을 때 (그냥 '/'기호 쓰면 실수로 출력됨)

print(2 ** 3) #거듭제곱
print (10%3)  # 나머지
print(10//3)  # 몫

# 비교 연산자 : 결과 불리안 자료형으로 출력됨 (True/False)
print(10>3)
print(4 >=7)
print(10<3)
print(5<=5)

print(not 10>3)
print(not 4 >=7)
print(not 10<3)
print(not 5<=5)

print(3==3) # 같다는 '='이 아닌 '=='임에 조심! '='은 대입한다는 뜻임. 
print(4==2)
print(3+4==7)
print(1!=3)

#논리 연산자 : 결과 불리안 자료형으로 출력됨 (True/False)
print ((3>0) and (3>5))
print ((3>0) or (3>5)) 
print (not 1!=3)

#단축 평가 : 논리 연산자에서 앞 연산의 결과에 따라 뒤 연산이 처리되지 않는 현상 (뒤에까지 안 봐도 결과 나올 때)
print (5>4>3)
print (4>5>3)

# 연산자의 우선순위
print (2+3*4)
print ((2+3)*4)

# 괄호 종류 (리스트, 딕셔너리, 세트, 튜플) -> 거듭제곱 -> 곱셈 나눗셈 -> 덧셈 뺄셈 -> 부정(not), 비교 -> 논리 (and/or) -> 대입 
# 괄산부비논대 / 산술 연산자는 수학이랑 같은데 거듭제곱이 먼저임

# 변수로 연산하기 
number = 2+3*4
print (number)
number = number + 2
print (number)

# 복합 대입 연산자 : 연산하고, 저장하라는 명령. '연산기호 =' 를 쓰면, 변수 재정의한 것과 같은 효과
number = 2+3*4 
print (number)
number += 2 # number = number + 2 와 동일 코드 # 16
print (number)

number = 2+3*4 
print (number)
number -= 2 # number = number - 2 와 동일 코드 # 12
print (number)

number = 2+3*4 
print (number)
number *=2  # number = number * 2 와 동일 코드 # 28
print (number)

number = 2+3*4 
print (number)
number /=2 # # number = number / 2 와 동일 코드 # 7.0
print (number)

number = 2+3*4 
print (number)
number %= 3 #number = number % 2 와 동일 코드 (나머지) #2
print (number)

number = 2+3*4 
print (number)
number //= 3 #number = number //3 와 동일 코드 (몫) #4
print (number)

# 함수로 연산하기
print(abs(-5))
print(pow(4,2)) #print(4**2)와 동일 코드
print(4**2)
print(max(5,12))
print(min(5,12))
print(round(3.14)) #두번째 인수 없으면, 반올림하여 정수로 표시 
print(round(4.678,2)) #두번째 인수 자리 '까지' 반올림하여 정수로 표시 ('에서' 반올림하는 것 아님.)

# 모듈 이용 방법 1 : from 모듈명 import 기능명 (*는 모든 기능)
from math import *

result = floor (4.99)
print(result)
result = ceil (3.14)
print(result)
result = sqrt (16)
print(result)

# 모듈 이용 2 : import 모듈명 (기능 쓸 때마다 모듈명.기능명 으로 명시)
import math
result = math.floor (4.99)
print (result)

result = math.ceil (3.14)
print (result)

result = math.sqrt(16)
print (result)

#random 모듈에 속하는 random 함수 : 0이상 1미만의 숫자를 무작위로 추출해 주는 함수 (난수 추출 기능)
from random import *
print(random())
print(random())
print(random())

import random
print(random.random())
print(random.random())
print(random.random())

from random import *
print(int(random()*10))
print(int(random()*10))
print(int(random()*10))

#0이상 n미만인 난수를 추출하는 방법 : random모듈의 random함수 이용 -> *n (0이상 n미만의 실수가 됨)-> int()로 형변환
from random import *
print(int(random()*45))
print(int(random()*45))
print(int(random()*45))

#0이상 n미만인 난수를 추출하는 방법 : random모듈의 random함수 이용 -> *n (0이상 n미만의 실수가 됨)-> int()로 형변환 -> +1
from random import *
print(int(random()*45)+1)
print(int(random()*45)+1)
print(int(random()*45)+1)

# random모듈의 범위 지정 함수 이용 : randrange(m,n) m이상 n미만 / randint(m,n) m이상 n이하
from random import *
print (randrange(1,46)) #m이상 n미만 
print (randint(1,45)) #m이상 n이하

# random 모듈의 sample()함수 이용 : 중복 제외한 난수 추출 가능 (제어문 배운 후 다시 학습 )

# 실습 문제 : 스터디 날짜 정하기 
# 풀이1
from random import *
date = randint(4,28)
print("오프라인 스터디 모임 날짜는 매월" ,date, "일로 선정됐습니다.")

# 풀이2
from random import *
date = randrange (4,29)
print("오프라인 스터디 모임 날짜는 매월" ,date, "일로 선정됐습니다.")

# 풀이3
from random import *
print("오프라인 스터디 모임 날짜는 매월" ,randint(4,28), "일로 선정됐습니다.")

# 풀이4
from random import *
print("오프라인 스터디 모임 날짜는 매월" ,randrange(4,29), "일로 선정됐습니다.")

#풀이5 : str() 이용한 형변환 하고, +로 연결하는 방법
from random import *
date = randint(4,28)
print("오프라인 스터디 모임 날짜는 매월" +str(date)+ "일로 선정됐습니다.")

# 셀프체크 : 온도 변환 프로그램 만들기 
# 풀이 :
celsius = 30
print("섭씨 온도 :" + str(celsius))
fahrenheit = (celsius * 9 / 5) + 32
print("화씨 온도 :" + str (fahrenheit))

celsius = 10
print("섭씨 온도 :" + str(celsius))
fahrenheit = (celsius * 9 / 5) + 32
print("화씨 온도 :" + str (fahrenheit))

