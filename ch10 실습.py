## 자동 주문 프로그램
chicken = 10 # 남은 치킨 개수
waiting = 1 #대기번호, 1부터 시작

class MaximumError(Exception):
    pass

class SoldOutError(Exception):
    pass


try:
    while True:
        print("[남은 치킨 : {0}]". format(chicken))
        order = int(input("치킨을 몇 마리 주문하시겠습니까?" ))
    
        if order > 10:
            raise MaximumError

        elif chicken == 0:
            raise SoldOutError

        elif order > chicken:
             print("재료가 부족합니다.")

        else:
            print("[대기번호 {0}] {1} 마리를 주문했습니다.". format(waiting, order))
            waiting += 1
            chicken = chicken - order #chicken -= order

except ValueError:
    print("값을 잘못 입력했습니다.")

except MaximumError:
    print("최대 주문량을 초과했습니다.")

except SoldOutError:
    print("재료가 소진돼 더 이상 주문을 받지 않습니다.")        


## 모범 답안
chicken = 10 # 남은 치킨 개수
waiting = 1 #대기번호, 1부터 시작

# while문을 try-except 안에 넣으면, 프로그램이 통째로 종료되므로 

while True:
    try:
        print("[남은 치킨 : {0}]". format(chicken))
        order = int(input("치킨을 몇 마리 주문하시겠습니까?" ))

        if order > chicken:
            print("재료가 부족합니다.")

        elif order <= 0: # 1보다 작은 수는 입력하지 못하도록 해야 함! (무결성 관점)
            raise ValueError

        else:
            print("[대기번호 {0}] {1} 마리를 주문했습니다.". format(waiting, order))
            waiting += 1
            chicken = chicken - order 


        if chicken == 0: ## if를 여러 개 쓰면 각 조건을 독립적으로 모두 검사하고, if-elif로 연결하면 위에서부터 검사해 처음 True인 조건만 실행한다.
            raise SoldOutError

    
    except ValueError:
        print("값을 잘못 입력했습니다.")

    except SoldOutError:
        print("재료가 소진돼 더 이상 주문을 받지 않습니다.")        
        break

## 셀프체크 모범답안

def save_battery(level):

    try:
            print("배터리 잔량 : {0}%".format(level))

            if level > 30:
                print("일반 모드로 사용합니다.")

            elif 5 < level <= 30:
                print("절전 모드로 사용합니다.")


            else:
                raise Exception("배터리가 부족해 스마트폰을 종료합니다.")

    except Exception as e:
        print(e)

save_battery(75)

save_battery(25)

save_battery(3)