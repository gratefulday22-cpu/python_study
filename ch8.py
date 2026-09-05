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