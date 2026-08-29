print(5)
print(-10)
print(3.14)
print(1000
      )

print(5+3)
print(2*8)
print(6/3)
print(3*(3+1))

print('풍선')
print('나비')
print('abcdefg')
print('10')
print('파이썬'*3)
print("I don't want to go to school.")

print(5>10)
print(5<10)
print(True)
print(False)

print(5<=10)
print(not True)
print(not 5>10)

# 변수 정의 후 사용, 가장 마지막에 정의된 변수로 출력함. 
name="해피"
animal="고양이"
age=4
hobby="낮잠"
is_male = True

# 변수 + "문자형" 로 연결. '+'기호는 자료형이 문자열인 변수만 연결 가능
print("반려동물을 소개해 주세요.")
print("우리집 반려동물은 " +animal+ "인데, " "이름은 " + name+ "에요.")
print(name+"은(는)" +str(age)+"살이고," +hobby+ "을(를) 아주 좋아해요.")
print(name+"은 수컷인가요?")
print("네.")

# ', '은 형 상관없이 연결 가능
print("반려동물을 소개해 주세요.")
print("우리 집 반려동물은 " ,animal , "인데, " "이름은 " ,name , "에요.")
print(name ,"은(는)" ,age ,"살이고," ,hobby ,"을(를) 아주 좋아해요.")
print(name ,"은 수컷인가요?")
print("네.")

# 형변환
print(int("3") , "입니다.")
print(int(3.5))
print(float("3.5") , "입니다.")
print(float(3))

print(3)
print(str(3) + "입니다.")
print(str(3.5)) + "입니다."
print(type(str(3.5)))
print(type(int(3.14)))

animal="고양이"
age=4
hobby="낮잠"
is_male = True


print("반려동물을 소개해 주세요.")
name="해피"
print("우리집 반려동물은 " +animal+ "인데, " "이름은 " + name+ "에요.")
print(name+"은(는)" + str(age)+ "살이고," +hobby+ "을(를) 아주 좋아해요.")
print(name+"은 수컷인가요?")
print("네.")

animal="고양이"
age=4
hobby="낮잠"
is_male = True


print("반려동물을 소개해 주세요.")
name="해피"
print("우리집 반려동물은 " +animal+ "인데, " "이름은 " + name+ "에요.")
hobby="수영"
print(name+"은(는)" + str(age)+ "살이고," +hobby+ "을(를) 아주 좋아해요.")
print(name+"은 수컷인가요?")
print("네.")

# %% 변수 정의 위치
animal="고양이"
age=4
hobby="낮잠"
is_male = True


print("반려동물을 소개해 주세요.")
name="해피"
print("우리집 반려동물은 " +animal+ "인데, " "이름은 " + name+ "에요.")
hobby="수영"
print(name+"은(는)" + str(age)+ "살이고," +hobby+ "을(를) 아주 좋아해요.")
print(name+"은 수컷인가요?")
print("네.")

# 실습문제 
station = "사당"
print(station+ "행 열차가 들어오고 있습니다.")
station = "신도림"
print(station+ "행 열차가 들어오고 있습니다.")
station = "인천공항"
print(station+ "행 열차가 들어오고 있습니다.")

#셀프체크
status = "상품 준비"
print("주문상태 : " + status)
status = "배송 중"
print("주문상태 : " + status)
status = "배송 완료"
print("주문상태 : " + status)