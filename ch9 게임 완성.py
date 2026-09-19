class Unit :
    def __init__(self, name, hp, speed):
        self.name = name 
        self.hp = hp
        self.speed = speed
        print("{0} 유닛을 생성했습니다.".format(name))

    def move(self, location):
        print("{0} : {1} 방향으로 이동합니다. [ 속도 {2}]".format(self.name,location, self.speed))


    def damaged(self, damage):
            print("{0} : {1} 만큼 피해를 입었습니다.".format(self.name, damage))
            self.hp = self.hp - damage
    
            print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
            if self.hp <= 0:
                print("{} : 파괴되었습니다.".format(self.name))

class AttackUnit(Unit):
    def __init__(self, name, hp, damage, speed):
         Unit.__init__(self, name, hp, speed)
         self.damage = damage

    def attack (self, location):
         print("{0} : {1} 방향 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))

# 보병 유닛
class Soldier(AttackUnit):
    def __init__(self):
          AttackUnit.__init__(self, "보병", 40 ,5, 1 )

    def booster(self):
         if self.hp >= 10:
              self.hp -=10
              print("{0} : 강화제를 사용합니다. (hp 10 감소)". format(self.name))

         else:
              print("{0} : 체력이 부족해 기술을 사용할 수 없습니다.". format(self.name))


# 탱크 유닛 
class Tank(AttackUnit):
     siege_developed = False # 시지 모드 개발 여부 : 클래스 변수로 정의 

     def __init__(self):
          AttackUnit.__init__(self, "탱크", 150, 35, 1)
          self.siege_mode = False # 시지 모드 (해제 상태) : 인스턴스 변수로 정의 

     def set_siege_mode(self):
        if Tank.siege_developed == False:
               return

        if self.siege_mode == False:
            print("{0} : 시지 모드로 전환합니다.".format(self.name))
            self.damage = self.damage * 2 # 공격력 2배
            self.siege_mode = True #시지 모드 활성화 상태 저장

        else:
            print("{0} : 시지 모드를 해제합니다.".format(self.name))
            self.damage = self.damage // 2
            self.siege_mode = False


class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly (self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}] ".format(name, location, self.flying_speed))

class FlyableAttackUnit (AttackUnit, Flyable):
    def __init__ (self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage, 0)
        Flyable.__init__(self, flying_speed)


    def move (self, location):
         self.fly(self.name, location)


class Stealth(FlyableAttackUnit):
     def __init__ (self):
          FlyableAttackUnit.__init__(self, "전투기", 80, 20, 5)
          self.cloaked = False #인스턴스 변수 정의, 은폐 모드 해제 상태

     def cloaking(self):
          if self.cloaked == True: # 현재 은폐 모드일 때
               print("{0} : 은폐 모드를 해제합니다.".format(self.name))
               self.cloaked = False

          else: 
               print("{0} : 은폐 모드를 설정합니다.".format(self.name))
               self.cloaked = True

## 게임 실행하기
def game_start():
     print("[알림] 새로운 게임을 시작합니다.")

def game_over():
     print("Player : Good Game")
     print("[Player] 님이 게임에서 퇴장했습니다.")

game_start()

so1 = Soldier()
so2 = Soldier()
so3 = Soldier()


ta1 = Tank()
ta2 = Tank()

st1 = Stealth()

# 유닛 일괄 관리
attack_units=[]
attack_units.append(so1)
attack_units.append(so2)
attack_units.append(so3)
attack_units.append(ta1)
attack_units.append(ta2)
attack_units.append(st1)

for unit in attack_units:
     unit.move("1시")


# 탱크 시지 모드 개발
Tank.siege_developed = True
print("[알림] : 탱크의 시지 모드 개발이 완료됐습니다.")

for unit in attack_units:
     if isinstance(unit, Soldier):
          unit.booster()

     elif isinstance(unit, Tank):
          unit.set_siege_mode()

     elif isinstance(unit, Stealth):
          unit.cloaking()


for unit in attack_units:
     unit.attack("1시")

from random import *

for unit in attack_units:
     unit.attack ("1시")

for unit in attack_units:
     unit.damaged(randint(5,20)) #5이상 20이하의 랜덤 정수로 피해 입음


game_over()
