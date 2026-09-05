## 함수 정의하기
# 동작만 포함하는 함수 정의 : 예제 - 계좌를 개설하는 함수 
def open_account():
    print("새로운 계좌를 개설합니다.")

open_account() #함수 호출 시, 정의된 함수 안에 있는 print()문이 실행된 것. 
# 함수를 호출할 때 : 함수명 () 


# 전달값과 반환값이 포함된 함수 정의하기 
# 계좌 개설 함수 정의
def open_account():
    print("새로운 계좌를 개설합니다.")

open_account() # 함수 호출

# 입금 처리 함수 정의
def deposit(balance,money): #함수 정의할 때 전달값 받는 변수 = 매개변수 
    print("{}원을 입금했습니다. 잔액은 {}원입니다.".format(money,balance+money))

    return balance+money

balance = 0
balance = deposit(balance, 1000) #deposit() 함수 호출하여 1000원 입금. 잔액에 저장됨

# 출금 처리 함수
def open_account(): #함수 정의
    print("새로운 계좌를 개설합니다.")
open_account() #함수 호출 

def deposit(balance,money): #함수 정의할 때 전달값 받는 변수 (balance, money 같은 것) = 매개변수 
    print("{}원을 입금했습니다. 잔액은 {}원입니다.".format(money,balance+money))

    return balance+money #반환값 저장 (이후 다른 코드에서 누적 가능)

def withdraw (balance,money):
    if balance >= money :
        print("{}원을 출금했습니다. 잔액은 {}원입니다.".format(money, balance - money))
        return balance-money # 출금 후 잔액 반환
    else:
        print("잔액이 부족합니다. 잔액은 {}원입니다.".format(balance))

balance = 3000
balance = withdraw(balance, 1000)

# 수수료 부과하기 
def open_account():
    print("새로운 계좌를 개설합니다.")

open_account()

def deposit(balance, money):
    print("{0}원을 입금했습니다. 잔액은 {1}원입니다.".format(money, balance + money))
    return balance + money

def withdraw_night (balance,money):
    commission = 100
    print("업무 시간 외에 {}원을 출금했습니다.".format(money))
    return commission, balance-money-commission

balance = 0
balance =  deposit (balance, 1000) # 입금 함수 호출하여 1000원 입금

commission, balance = withdraw_night(balance,500)
print("수수료 {}원이며, 잔액은 {}원입니다.".format(commission, balance))

# 함수 호출 : 기본값 사용하기 
def profile(name, age, main_lang):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))

profile("찰리", 20, "파이썬")
profile("루시", 25, "자바")

# 함수 정의할 때 기본값 지정 시, 입력값에 인자 입력하지 않으면 기본값으로 출력
def profile(name, age=20, main_lang="파이썬"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))

profile("찰리")
profile("루시")

# 기본값이 있어도 전달값을 입력하면, 전달값으로 출력 
def profile(name, age=20, main_lang="파이썬"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))

profile("찰리", 25, "영어")
profile("루시", 28, "한국어")

# 기본값 설정하는 전달값보다, 일반 전달값 (기본값 없는)을 항상 먼저 적어야 함. 
def buy(item1="빵", item2): # 오류 발생
    print(item1, item2)

buy("사과")

# 키워드 인자 사용하기 : 함수 호출할 때, 어떤 매개변수에 어떤 전달값을 전달할지 위치를 지정 (순서에 구애받지 않고 쓸 수 있음)
def profile (name, age, main_lang):
    print(name, age, main_lang)

profile (name="찰리", main_lang="파이썬", age = 20)
profile (main_lang="자바", age = 25, name = "루시")
profile (name="아이언맨")
profile(age=21, name="슈퍼맨")
profile(name="루시", 25, "파이썬") # 키워드 인자를 먼저 작성하면 안 됨. 
profile("루시", age=21, name="슈퍼맨") #일반 전달값 먼저 작성해야


# end의 기본값은 줄바꿈 (\n), end 매개변수에 다른 전달값 전달 시 줄바꿈 다신 사용 가능
def profile (name, age, lang1, lang2, lang3, lang4, lang5):
    print ("이름 : {0}\t나이 : {1}\t".format(name, age))
    print(lang1, lang2, lang3, lang4, lang5)

profile("찰리", 20, "파이썬", "자바", "C", "C++", "c#")
profile("루시", 25, "코틀린", "스위프트", "","","")

def profile (name, age, lang1, lang2, lang3, lang4, lang5):
    print ("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") #줄바꿈 대신 띄어쓰기 하고 다름 print()문 이어서 출력
    print(lang1, lang2, lang3, lang4, lang5)

profile("찰리", 20, "파이썬", "자바", "C", "C++", "c#")
profile("루시", 25, "코틀린", "스위프트", "","","")

# 가변 인자 - 전달값 개수에 관계없이 묶어서 튜플로 인식함. 
def profile (name, age, *language):
    print ("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    print(language, type(language))

profile("찰리", 20, "파이썬", "자바", "C", "C++", "c#", "자바스크립트")
profile("루시", 25, "코틀린", "스위프트")

#튜플 형태가 아닌 값을 하나씩 출력하려면 : for문을 이용
def profile (name, age, *language):
    print ("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")

    for lang in language:
        print(lang, end="") #줄바꿈 대신 띄어쓰고 다음 문장 실행
    print()

profile("찰리", 20, "파이썬", "자바", "C", "C++", "c#", "자바스크립트")
profile("루시", 25, "코틀린", "스위프트")

#함수 안에서 함수 호출하기 (어떤 함수 정의 후 실행 동작으로서, 다른 함수 호출할 수 있음)
def add(item):
    print(item, "붓기")

def americano():
    add("뜨거운 물")
    add("에스프레소")

print("아메리카노 만드는 법")
americano()

# 지역변수와 전역변수 
glasses = 10 # 전역변수 

def rent(people):
    glasses = 20 # 지역변수 
    glasses = glasses - people
    print("[함수 내부] 남은 3D 안경 개수 : {}".format(glasses))

print("전체 3D 안경 개수 : {}".format(glasses))
rent(6)
print("남은 안경 개수 :{}".format(glasses))

glasses = 10 # 전역변수 

def rent(people):
    global glasses # 전역변수 (glasses = 10 이라고 정의한 값)를 함수 안에서 사용하겠다 
    glasses = glasses - people
    print("[함수 내부] 남은 3D 안경 개수 : {}".format(glasses))

print("전체 3D 안경 개수 : {}".format(glasses))
rent(6)
print("남은 안경 개수 :{}".format(glasses))

# 전역변수를 global로 함수 내로 호출하는 것은 되도록 지양. 전역변수 없는 버전으로 만들기
glasses = 10

def rent_return(glasses, people): #전체 안경 수, 대여 관객 수를 전달값으로 전달 받음. 
    glasses = glasses - people
    print("[함수 내부] 남은 3D 안경 개수 : {}".format(glasses))
    return glasses

print("전체 3D 안경 개수 : {}".format(glasses))
glasses = rent_return(glasses, 2) #함수 안에서 수정된 glasses 값을 반환 받음
print("남은 안경 개수 :{}".format(glasses))

# 실습 문제
# 처음 풀이 # if문 들여쓰기 해야 함!! 
def std_weight(height, gender):
    if gender == "남자":
    x = height * height * 22

    elif gender == "여자":
    x = height * height * 21

    print("키 {}cm {}의 표준 체중은 {}kg 입니다". format(height,gender,round(x,2)))

std_weight(1.75,"남자")

# 수정 _ 1차 : 아직 단위 문제가 
def std_weight(height, gender):
    if gender == "남자":
        x = height * height * 22

    elif gender == "여자":
        x = height * height * 21

    print("키 {}cm {}의 표준 체중은 {}kg 입니다". format(height*100,gender,round(x,2)))

std_weight(1.75,"남자")

# 수정 _ 2차
def std_weight(height, gender):
    if gender == "남자":
        x = height * height * 22

    elif gender == "여자":
        x = height * height * 21

    print("키 {}cm {}의 표준 체중은 {}kg 입니다". format(height*100,gender,round(x,2)))

std_weight(1.75,"남자")

# 수정_3차
def std_weight(height, gender):
    if gender == "남자":
        x = height * height * 22

    elif gender == "여자":
        x = height * height * 21

    print("키 {}cm {}의 표준 체중은 {}kg 입니다". format(int(height*100),gender,round(x,2)))

std_weight(1.75,"남자")

# 해설 (모범코드)
def std_weight(height, gender):
    if gender == "남자":
        return height * height * 22 #if문 안에서 새로운 변수를 정의하지 않고 함수 밖으로 값을 돌려준 것. 
    else:
        return height * height * 21 # 여기서 height은 지역변수

height = 175 # 함수 호출하기 전에 전역 변수의 값 정의 (호출하면서 지역변수가 175를 전달받음)
gender = "남자"
weight = round(std_weight(height /100, gender),2) #weight라는 변수를 정의할 때 함수를 호출 
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))

## 챗 GPT 코멘트
# 처음 푸신 코드는 함수 안에서 계산 결과를 x(지역변수)에 저장하고 함수 안에서 출력까지 한 것, 
# 모범답안은 계산 결과를 return(반환값으로 함수 밖으로 돌려줌)해서 함수 밖에서 활용하도록 만든 것이라는 차이입니다.

# 셀프체크 : 미세먼지 수치 입력받아 대기질 상태 출력하는 함수 작성
def get_air_quality(air):
    if 0 <= air <= 30:
        print("좋음")
    elif 31 <= air <= 80:
        print("보통")
    elif 81 <= air <= 150:
        print("나쁨")
    else:
        print("매우 나쁨")

print (get_air_quality(15))


# 수정 코드 : None 안 뜨게 하려면, print()없이 바로 함수명 호출!
def get_air_quality(air):
    if 0 <= air <= 30:
        print("좋음")
    elif 31 <= air <= 80:
        print("보통")
    elif 81 <= air <= 150:
        print("나쁨")
    else:
        print("매우 나쁨")

get_air_quality(90)

# 챗 GPT 코멘트
# air 는 매개변수, 호출할 때 입력하는 인자 (argument)가 값으로 전환값에 전달되는 것
# 출력 결과를 함수 밖에서 활용하고 싶다면, return 을 써서 반환값 정의