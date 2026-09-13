## 입출력 
## % 표준 입력 : input()함수 - 키보드로 바로 입력받아 사용 (입력값의 자료형은 항상 문자열로 인식한다는 점에 유념 !)

answer = input("아무 값이나 입력하세요 : ")
print("입력한 값은" + answer + "입니다.") #항상 문자열로 인식. 오히려 이를 숫자 연산에 사용하려면 int()로 형변환 필요
print(type(answer))

answer = input("아무 값이나 입력하세요 : ") #항상 문자열로 인식. 오히려 이를 숫자 연산에 사용하려면 int()로 형변환 필요
print("입력한 값은" + answer + "입니다.")
print(type(answer)) # <class:str>
print(type(int(answer)))


answer = 10
print(type(answer)) # <class:int>

## % 표준 출력 : print()함수 
# 구분자 넣기 : sep 매개변수 
print("파이썬", "자바")
print("파이썬" + "자바")
print("파이썬", "자바", sep= ",") #문자열 구분 기호로 sep 매개변수 활용하여 , 지정 -> 값을 ,로 구분
print("파이썬", "자바", "자바스크립트", sep= " vs ") #값을 vs로 구분

# 문장 끝 지정하기 : end 매개변수 (기본값은 줄 바꿈 \n)
print("파이썬", "자바", sep= ", ", end = "? ") #end 지정했으므로 ? 로 연결 후 한 줄로 출력
print("무엇이 더 재미있을까요?")

print("파이썬", "자바", sep= ", ") #end 기본값이 줄바꿈이므로 서로 다른 print()문 두 줄에 걸쳐 출력
print("무엇이 더 재미있을까요?")

# 출력 위치 지정하기 : file
import sys

print("파이썬", "자바", file = sys.stdout) #표준 출력 (터미널에 출력)
print("파이썬", "자바", file = sys.stderr) #오류 출력 (터미널에 오류 메시지)

# 공간 확보해 정렬하기 : ljust()와 rjust()
scores = {"수학":0, "영어":50, "코딩":100}

for subject, score in scores.items(): #items()는 key와 value 모두 가져오는 메서드  
    print(subject, score)


scores = {"수학":0, "영어":50, "코딩":100}

for subject, score in scores.items(): #items()는 key와 value 모두 가져오는 메서드  
    print(subject.ljust(8), str(score).rjust(4),sep = ":") #정렬하는 값은 문자열이어야 함! ()안의 값만큼 공간 확보하고 정렬

#빈칸 0으로 채우기 : zfill()
for num in range(1,21):
    print("대기번호 :" + str(num))

for num in range(1,21):
    print("대기번호 :" + str(num).zfill(3)) #()안의 값만큼 문자열 앞을 0으로 채움 

##% 다양한 형식으로 출력하기 : format {}
# {:채울 문자 정렬 공간수}
print("{0}".format(500))
print("{0: >10}".format(500)) # 우측 정렬
print("{0:>10}".format(500))
print("{0:_>10}".format(500))

print("{0: <10}".format(500)) # 좌측 정렬
print("{0:<10}".format(500))
print("{0:_<10}".format(500))

# 양수일 때 부호 표시
print("{0: >+10}".format(500))
print("{0: >10}".format(-500))

# #,##0 (자릿수 표시)
print("{0:,}".format(100000000))
print("{0:+,}".format(100000000)) # 양수일 때 +로 표시하려면 
print("{0:+,}".format(-100000000)) 

# 복잡 예제 
print("{0:^<+30,}".format(100000000))

# [정리하면] 콜론 뒤에 순서 : 채울 문자 -> 정렬 방향 -> + -> 칸 수 -> , 순서
# 소수점을 포함하는 실수 출력
print("{0}".format(5/3))
print("{0:f}".format(5/3)) # 소수점 아래 6자리까지만 표시 : 콜론 뒤에 f
print("{0:.2f}".format(5/3)) # 소수점 아래 n자리까지만 표시 : 콜론 뒤에 .nf

## % 파일 입출력
# 쓰기 모드
score_file = open("score.txt","w",encoding="utf8")
print("수학 : 0", file=score_file)
print("영어 : 50", file = score_file)
score_file.close()

# 이어 쓰기 모드
score_file = open("score.txt", "a", encoding="utf8")
score_file.write("과학 : 80\n" )
score_file.write("코딩 : 100\n" )
score_file.close()

#읽기 모드 
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read()) # 파일 전체 읽어 와서 터미널에 출력
score_file.close()

# 한 줄씩 읽기 : readline() 함수 사용 + while문과 함께
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline() #score_file에서 한 줄씩 읽어온 값을 line 변수로 정의 
    if not line: # 더 이상 읽어 올 내용이 없을 때
        break # 탈출하세요
    print (line, end="")

score_file.close()

# 한꺼번에 파일 불러와서 리스트에 저장하고, 한 줄씩 출력 + for문과 함께
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() #score_file에서 한 줄씩 읽어온 값을 lines 라는 리스트에 저장 
for line in lines:
    print(line, end="")

score_file.close()


# 데이터를 파일에 저장하기 : pickle 모듈
import pickle 
profile_file = open("profile.pickle", "wb") # 파일 열기 (바이너리 형태, 쓰기 모드)
profile = {"이름":"스누피", "나이":30, "취미":["축구","골프","코딩"]} # 변수 딕셔너리로 정의 
print(profile)

pickle.dump(profile, profile_file) #dump함수로 파일 저장하기 (pickle모듈에 있는 dump 함수 실행, 변수명 -> 파일명에 저장)
profile_file.close() # 파일 닫기 

# 파일 불러오기

import pickle
profile_file = open("profile.pickle","wb") #변수 profile_file 에 profile.pickle이라는 파일을 열고, 열린 그 객체를 저장
profile = {"이름":"스누피", "나이":30, "취미":["축구","골프","코딩"]} # 변수 profile에 딕셔너리 데이터 저장
print(profile)

pickle.dump(profile, profile_file) #pickle모듈의 dump함수 이용해서, profile 변수의 데이터(딕셔너리)를 profile_file 변수(파일)에 저장
profile_file.close() # 파일 닫기

profile_file = open("profile.pickle","rb")
profile = pickle.load(profile_file)

print(profile)
profile_file.close()

# 파일 한 번에 열고 닫기 : with 문
## 참고 : 파이썬 객체를 저장 가능한 바이트 형태로 바꾸고, 나중에 다시 원래 파이썬 객체로 복원하는 기능을 모아둔 모듈
#음식을 피클로 만들어 보존해두었다가 나중에 먹는 것처럼, Python 객체를 pickle해서 보존해두었다가 나중에 다시 꺼내 쓴다.


import pickle #pickle이라는 모듈 자체를 모두 가져옴 cf) from 모듈명 import * (또는 함수명) 써도 됨

with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file)) #사용 시 모듈명.함수()로 사용

import pickle
with open("study.txt", "w", encoding="utf8") as study_file: #study.txt 라는 파일을, 쓰기 모드로 열어서 study_file 이라는 변수에 저장
    study_file.write("파이썬을 열심히 공부하고 있어요.") #study_file이라는 변수에 write 기능 실행. (파일에 저 문자열이 쓰여짐)

with open("study.txt","r",encoding="utf8") as study_file: # #study.txt 라는 파일을, 읽기 모드로 열어서 study_file 이라는 변수에 저장
    print(study_file.read()) #study_file이라는 변수에 read 기능 실행 (읽어오기)

 ## 실습 문제 : 보고서 파일 만들기
for week in range(1,51):
    weekly_file = open("{}주차.txt".format(week), "w", encoding="utf8") #파일명 이후에 계속 사용해야 하므로 변수에 담음
    print("-{}주차 주간보고-".format(week), file=weekly_file)
    print("부서 : ", file=weekly_file)
    print("이름 : ", file=weekly_file)
    print("업무 요약 : ", file=weekly_file)

    weekly_file.close()

# 모범답안 : with문 활용
for i in range(1,51):
    with opne(stt(i) + "주차.txt", "w", encoding="utf8") as report_file:
    report_file.write("-{}주차 주간보고-".format(i))
    report_file.write("\n부서: ")
    report_file.write("\n 이름: ")
    report_file.write("\n 업무: ")

# 셀프체크

class_file = open("class.txt", "w", encoding="utf8")
print("초록반 5세 20명 파랑반 6세 18명 노랑반 7세 22명", file= class_file)

class_file = open("class.txt", "r", encoding="utf8")
print(class_file.read())
class_file.close()

# 모범답안
with open("class.txt", "r", encoding="utf8") as f: # class.txt 라는 이름의 파일 읽기 모드로 열어서 f라는 변수에 저장
    txt = f.read() # 파일 전체 읽어 와서 txt라는 변수에 저장
    words = txt.split() #파일을 빈칸으로 구분

for word in words:
    print(word, end="")
    if word.endswith("명"):
        print()