## 패키지 다루기
# 방법1 : import 모듈명 as 별칭
# 사용 시 모듈명(또는 별칭). 함수명()

import theater_module as mv

mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)


# 방법2 : from 모듈명 import 기능(함수명)
# 사용 시 바로 함수명()
from theater_module import *

price (3)
price_morning(4)
price_soldier(5)

# 사용하려는 함수만 부르는 경우
from theater_module import price, price_morning

price (3)
price_morning(4)

# 별칭 추가 가능
from theater_module import price_soldier as price

price (5)


## 패키지 다루기
# 방법1 : import 패키지명. 모듈명
import travel.thailand

trip_to = travel.thailand.ThailandPackage
trip_to.detail()


# 방법2 : from 패키지명. 모듈명 import 클래스명
from travel.thailand import ThailandPackage

trip_to = ThailandPackage
trip_to.detail()


from travel.thailand import ThailandPackage

# 방법3 : from 패키지명 import 모듈명
from travel import vietnam

trip_to = vietnam.VietnamPackage()
trip_to.detail()

## 모듈 공개 설정하기 : __all__
from travel import *

# trip_to = vietnam.VietnamPackage()
trip_to = thailand.Thailandpackage()
trip_to.detail()


## 모듈 직접 실행하기 
from travel import *

trip_to = thailand.ThailandPackage()
trip_to.detail()

# 패키지와 모듈 위치 확인하기
import inspect
import random

print(inspect.getfile(random)) #inspect라는 이름의 모듈에서 getfile함수를 실행해서 random모듈의 경로를 확인

import inspect
from travel import *

print(inspect.getfile(thailand))

## 파이썬 내장 함수 
language = input("어떤 언어를 좋아하세요? ")
print("{0}은 아주 좋은 언어입니다!".format(language))

print(dir()) # 아무것도 안 했을 때
import random

print(dir()) # random 모듈 가져다 썼을 때
import pickle

print(dir()) # pickle 모듈 가져다 썼을 때

import random
print(dir(random)) #특정 모듈을 직접 dir()함수의 전달값으로 넘기면, 어떤 변수와 함수를 가지고 있는지 알려 줌

lst = [1,2,3]
print(dir(lst))

name = "Jim"
print(dir(name))

## 외장 함수 사용
import glob
print(glob.glob("*.py"))

import os
print(os.getcwd())


import os
folder = "sample_dir"
if os.path.exists(folder): #path는 또 다른 모듈, 모듈끼리 연결할 때 .으로 연결
    print("이미 존재하는 폴더입니다.")

else:
    os.makedirs(folder)
    print(folder, "폴더를 생성했습니다.")


# 같은 이름의 파일이 있으면 해당 파일 삭제하도록 
import os

folder = "sample_dir"
if os.path.exists(folder): #path는 또 다른 모듈, 모듈끼리 연결할 때 .으로 연결
    print("이미 존재하는 폴더입니다.")
    os.rmdir(folder)
    print(folder, "폴더를 삭제했습니다.")

else:
    os.makedirs(folder)
    print(folder, "폴더를 생성했습니다.")

# 현재 작업 폴더 안에 있는 폴더와 파일 목록 출력
import os

print(os.listdir())


# 시간 관련 모듈
import time
print(time.localtime())

import time
print(time.strftime("%Y-%m-%d %H:%M:%S")) #월, 일만 소문자로

import datetime
print("오늘 날짜는", datetime.date.today())

# 날짜 카운트 
import datetime
today = datetime.date.today() # 오늘 날짜를 today라는 변수에 저장함
td = datetime.timedelta(days=100) #100일의 시간 간격 저장

print("우리가 만난 지 100일은", today + td)

# 실습 문제
import byme
byme.sign()

#셀프체크
import greeting
greeting.say_hello("파이썬")
greeting.say_goodbye("나도코딩")