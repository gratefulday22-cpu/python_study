
## try - except 문
try: 
    print("나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))

    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))

except ValueError:
    print("오류 발생! 잘못된 값을 입력했습니다.")


## 오류 메시지를 예외 처리로 출력하기 : as
try: 
    print("나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))

    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))

except ValueError:
    print("오류 발생! 잘못된 값을 입력했습니다.")

except ZeroDivisionError as err: #발생한 에러 종류를 err 라는 변수에 저장해서 객체로 갖고 있도록 명령
    print(err)

# 입력받는 값 num1, num2와 나눗셈 결과를 리스트에 저장할 경우
try: 
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : "))) # 리스트의 인덱스 0번으로 첫 번째 입력값 저장
    nums.append(int(input("두 번째 숫자를 입력하세요 : "))) # 리스트의 인덱스 1번으로 첫 번째 입력값 저장
    nums.append(int(nums[0] / nums[1])) # 리스트의 인덱스 2번으로 나눗셈 결과 저장
    print("{0} / {1} = {2} ". format(nums[0], nums[1], nums[2]))

except ValueError:
    print("오류 발생! 잘못된 값을 입력했습니다.")

except ZeroDivisionError as err: 
    print(err)

except Exception as err:
    print("알 수 없는 오류가 발생했습니다.")
    print(err)

## 오류 발생시키기 
try: 
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >=10:
        raise ValueError
    
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))

except ValueError:
    print("값을 잘못 입력했습니다. 한 자리 숫자만 입력하세요.") 


## 사용자 정의 예외 처리하기
class BigNumberError(Exception): #파이썬에 포함된 클래스 상속
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >=10:
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))

except ValueError:
    print("값을 잘못 입력했습니다. 한 자리 숫자만 입력하세요.")

except BigNumberError as err:
    print("오류가 발생했습니다. 한 자리 숫자만 입력하세요.")
    print(err)

## 구체적인 오류 메시지 출력
class BigNumberError(Exception): #파이썬에 포함된 클래스 상속
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return "[오류 코드 001]" + self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >=10:
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))

except ValueError:
    print("값을 잘못 입력했습니다. 한 자리 숫자만 입력하세요.")

except BigNumberError as err:
    print("오류가 발생했습니다. 한 자리 숫자만 입력하세요.")
    print(err)

## 오류와 상관없이 무조건 실행하기 : finally
class BigNumberError(Exception): #파이썬에 포함된 클래스 상속
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return "[오류 코드 001]" + self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >=10:
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))

except ValueError:
    print("값을 잘못 입력했습니다. 한 자리 숫자만 입력하세요.")

except BigNumberError as err:
    print("오류가 발생했습니다. 한 자리 숫자만 입력하세요.")
    print(err)

finally:
    print("계산기를 이용해 주셔서 감사합니다.")