## 문자열이란?
sentense1 = '나는 소년입니다.'
print(sentense1)

sentense2 = "파이썬은 쉬워요."
print(sentense2)

sentense1 = '나는 소년입니다.'
print(sentense1, type(sentense1))

sentense2 = "파이썬은 쉬워요."
print(sentense2, type(sentense2))

sentense3 = """
나는 소년이고, 
파이썬은 쉬워요.
"""

print(sentense3)

## 슬라이싱
jumin = "990229-1234567"
print("성별 식별번호 : " + jumin[7]) #변수명[인덱스번호] (인덱스 셀 때 공백도 문자 하나로 취급)

jumin = "990229-1234567"
print("연 :" +jumin[0:2]) #끝 번호 미포함
print("월 :" +jumin[2:4])
print("일 :" +jumin[4:6])

jumin = "990229-1234567"
print("생년월일 : " +jumin[:6])
print("주민등록번호 뒷자리 : " + jumin[8:])
print(jumin[:])

jumin = "990229-1234567"
print("주민등록번호 뒷자리 (뒤에서부터) : " + jumin[-7])

## 함수로 문자열 처리하기 : print(변수명.함수명())
python = "Python is Amazing"
print(python.lower()) #전체 소문자로 전환
print(python.upper()) #전체 대문자로 전환
print(python[0].isupper()) #대문자인지 확인 
print(python[1:3].islower()) #소문자인지 확인
print(python.replace("Python", "Java")) #첫 번째 인수의 문자열을 두 번째 인수의 문자열로 대체 (replace ("a","b"))

#문자열 내에서 특정 문자의 인덱스를 찾는 함수 : find, index (찾는 문자, 시작 인덱스, 종료 인덱스)
#find함수
python = "Python is Amazing"
print(python.find("n")) #python 변수의 문자열 내에서 처음으로 발견하는 'n'의 인덱스 번호 반환
find = python.find("n") #python 변수의 문자열 내에서 처음으로 발견하는 'n'의 인덱스 번호를 find라는 이름의 변수에 저장
print(find)
find = python.find("n", find+1) #find+1 = 6이므로, 시작 인덱스 = 6으로 설정한 범위 내에서 'n'의 인덱스 번호 찾아서 저장
print(find)
find = python.find("Java")
print(find) #찾는 문자열이 없으면, -1 반환 후 프로그램 계속 실행

#index
python = "Python is Amazing"
print(python.index("n"))
index = python.index("n") #python 변수의 문자열 내에서 처음으로 찾은 'n'의 인덱스 번호를 index라는 이름의 변수에 저장
print(index)
index = python.index("n",index+1) #index+1 = 6이므로, 시작 인덱스 = 6으로 설정한 범위 내에서 'n'의 인덱스 번호 찾아서 저장
print(index)
index=python.index("Java")
print(index) #범위 내 찾는 문자열이 없으면, 에러 발생 후 프로그램 종료 

#count함수 : 문자열 내 지정한 문자 또는 문자열의 횟수 세는 함수
python = "Python is Amazing"
print(python.count("n"))
print(python.count("v"))

#len() 함수 : 문자열의 길이 세는 함수 
# ㄴ 일반적인 함수와 다르게, 문자열.함수() 형태가 아닌 함수 안에 문자열 또는 변수명을 바로 넣음
python = "Python is Amazing"
print(len(python))

#문자열 포매팅
#방법1 : 서식지정자 사용 : 빈칸을 %s로 표시, "문자열" %빈칸에 들어갈 값 (문자형 또는 문자열이면 따옴표로 감싸서)
print("나는 %d살입니다." %20) # %d : 정수
print("내 점수는 %f점입니다." %82.5) # %f : 실수
print("나는 %s을 좋아합니다." %'파이썬') # %s : 문자열
print("Apple은 %c로 시작해요." %'A') # %c : 문자

print("내 점수는 %s점입니다." %82.5) # %s 사용 시 뭐든지 출력 가능
print("내 점수는 %f점입니다." %82.5) # %f : 실수
print("내 점수는 %.2f점입니다." %82.5) # %.nf : 실수 (소수점 이하 n째자리까지 반올림 )

print("나는 %s색과 %s색을 좋아해요."% ("파란", "빨간")) #서식지정자 여러 개 사용

#방법2 : format() 함수 사용
print("나는 {}살입니다". format(20))
print("나는 {}색과 {}색을 좋아해요". format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요".format("파란", "빨간"))

print("나는 {age} 살이며, {color}색을 좋아해요". format(age=20,color='빨간'))
print("나는 {age} 살이며, {color}색을 좋아해요". format(color='빨간',age=20))

#방법3 : f- 문자열 사용
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

#print(f"문자열") 이런 식으로 쓰고, 변수명은 중괄호 안에 넣기. 문자열 전에 지정한 변수를 사용 가능. 

# 탈출 문자
print("백문이 불여일견 백견이 불여일타")
print("백문이 불여일견\n백견이 불여일타") #\n : 문자열 내에서 줄바꿈
print("저는 \"나도코딩\" 입니다.") # \뒤에 있는 문자는 문자 자체로 인식하도록 
print("C:\\Users\\Nadocoding\\Desktop\\Pythonworkspace") # 파일 경로 출력 등 \ 자체를 문자 자체로 인식하도록 하고 싶을 땐 \\
print(r"C:\Users\Nadocoding\Desktop\Pythonworkspace") #"문자열" 앞에 r붙이면, 무조건 해당 문자열 그대로 출력. 
print("Red Apple\r Pine") #\r : 커서 맨 앞으로 이동하여 \r 뒤에 오는 문자로 덮어써서 출력
print("Redd\b Apple") #\b : 커서를 한 칸 앞으로 이동 후 다음에 오는 한 글자를 삭제 
print("Red\tApple") #\t : 여러 칸 띄어 쓰는 역할

# 실습 문제 : 비밀번호 만들기 
# 풀이1 (260827 오전)
naver_1 = "http://naver.com"
print(naver_1+ "의 비밀번호는" +naver_1[7:10] + str(len(naver_1[7:12])) +str('naver'.count('e'))+"!" + "입니다.")

daum_1 = "http://daum.net"
print(daum_1+ "의 비밀번호는" +daum_1[7:10] + str(len(daum_1[7:11])) +str('daum'.count('e'))+"!" + "입니다.")

google_1 = "http://google.com"
print(google_1+ "의 비밀번호는" +google_1[7:10] + str(len(google_1[7:13])) +str('google'.count('e'))+"!" + "입니다.")

youtube_1 = "http://youtube.com"
print(youtube_1+ "의 비밀번호는" +youtube_1[7:10] + str(len(youtube_1[7:14])) +str('youtube'.count('e'))+"!" + "입니다.")


# 풀이2 (260827 오후)
url = "http://naver.com"
site=url[7:url.find('.')]
print(site) #naver

password = site[:3]+str(len(site))+str(site.count('e'))+"!"
print(url+ "의 비밀번호는" +password+ "입니다.")

url = "http://daum.net"
site=url[7:url.find('.')]
print(site) #daum

password = site[:3]+str(len(site))+str(site.count('e'))+"!"
print(url+ "의 비밀번호는" +password+ "입니다.")

url = "http://google.com"
site=url[7:url.find('.')]
print(site) #google

password = site[:3]+str(len(site))+str(site.count('e'))+"!"
print(url+ "의 비밀번호는" +password+ "입니다.")

url = "http://youtube.com"
site=url[7:url.find('.')]
print(site) #youtube

password = site[:3]+str(len(site))+str(site.count('e'))+"!"
print(url+ "의 비밀번호는" +password+ "입니다.")

# GPT 코멘트 : 하드코딩 (상황에 따라 변할 수 있는 값을 고정해 두는 것)을 줄이는 식으로 사고하는 연습하기 !! 

#정답
url = "http://naver.com"
my_str=url.replace("http://","") #앞부분 공백으로 대체 "naver.com"만 남음
my_str=my_str[:my_str.index('.')] #naver
password=my_str[:3] + str(len(my_str)) + str(my_str.count('e'))+"!"
print("{0}의 비밀번호는 {1}입니다.".format(url,password)) #format함수 사용

## 셀프체크 : 어떤 문장이 주어졌을 때, 첫 글자만 대문자로 표시하고 나머지는 소문자로 바꾸는 프로그램 작성
sentence = "the early bird catches the worm."
first = sentence[0:1] #문장의 첫 글자
others = sentence[1:] #문장의 나머지 글자 
print(others)
print(first.upper()+others.lower())

sentence = "Actions Speak Louder Than Words."
first = sentence[0:1] #문장의 첫 글자
others = sentence[1:] #문장의 나머지 글자 
print(others)
print(first.upper()+others.lower())

sentence = "PRACTICE MAKES PERFECT."
first = sentence[0:1] #문장의 첫 글자
others = sentence[1:] #문장의 나머지 글자 
print(others)
print(first.upper()+others.lower())

## GPT 피드백 1 - capitalize() 메서드 활용 
sentence = "the early bird catches the worm."
print(sentence.capitalize())

sentence = "Actions Speak Louder Than Words."
print(sentence.capitalize())

sentence = "PRACTICE MAKES PERFECT."
print(sentence.capitalize())


## GPT 피드백 2 - for 반복문 활용해서 반복되는 코드 단축 가능
sentences = [
    "the early bird catches the worm.",
    "Actions Speak Louder Than Words.",
    "PRACTICE MAKES PERFECT."
]

for sentence in sentences:
    print(sentence.capitalize())