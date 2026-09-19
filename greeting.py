name = input("이름을 입력하세요 :")
print("안녕, {0}?".format(name))
print("또 만나, {0}!".format(name))

## 모범답안
def say_hello(to): #to는 전달값 저장하는 매개변수
    print(f"안녕, {to}?")

def say_goodbye(to):
    print(f"또 만나, {to}!")

if __name__ == "__main__":
    say_hello("파이썬")
    say_goodbye("나도코딩")