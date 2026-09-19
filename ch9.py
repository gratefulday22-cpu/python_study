name = "보병"
hp = 40
damage = 5

print("{} 유닛을 생성했습니다.".format(name))
print("체력 {0}, 공격력 {1}".format(hp, damage))

tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("{} 유닛을 생성했습니다.".format(tank_name))
print("체력 {0}, 공격력 {1}".format(tank_hp, tank_damage))


tank2_name = "탱크"
tank2_hp = 150
tank2_damage = 35

print("{} 유닛을 생성했습니다.".format(tank2_name))
print("체력 {0}, 공격력 {1}\n".format(tank2_hp, tank2_damage))

def attack(name,location,damage):
    print("{0}:{1} 방향 적군을 공격합니다. [공격력 {2}]".format(name,location,damage))

attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)
attack(tank2_name, "1시", tank2_damage)

## 클래스 
# 클래스 만들기 
class Unit: # 클래스명 (대문자로 시작)
    def __init__(self, name, hp, damage): # 클래스 안에 메서드 정의 (들여쓰기 후) / 메서드 = 함수
        self.name = name # 메서드 안에 인스턴스 변수 정의 (들여쓰기 후)
        self.hp = hp
        self.damage = damage
        print("{} 유닛을 생성했습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

soldier1 = Unit("보병", 40, 5) 
soldier2 = Unit("보병", 40, 5)
tank = Unit("탱크", 150, 35)

# 생성자 : __init__() - self 제외한 전달값 개수만큼 넘겨 주면서 객체 정의해야 함. 

stealth1 = Unit("전투기", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(stealth1.name, stealth1.damage))
stealth2 = Unit("업그레이드한 전투기", 80, 5)
stealth2.cloaking = True
if stealth2.cloaking == True:
    print("{}는 현재 은폐 상태입니다.".format(stealth2.name)) # 객체 stelath2 만을 위한 변수 정의 (클래스 외부에서 별도로)

if stealth1.cloaking == True:
    print("{}는 현재 은폐 상태입니다.".format(stealth1.name)) # 오류 발생

## 메서드 
class AttackUnit:
    def __init__(self, name, hp, damage): # 메서드 (생성자)
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향 적군을 공격합니다. [공격력 {2}]"\
              .format(self.name, location, self.damage))

    def damaged(self, damage):
        # 피해 정보 출력
        print("{0} : {1} 만큼 피해를 입었습니다.".format(self.name, damage))
        self.hp = self.hp - damage

        # 남은 체력 출력
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{} : 파괴되었습니다.".format(self.name))


flamethrower1 = AttackUnit("화염방사병", 50, 16)
flamethrower1.attack("5시")

flamethrower1.damaged(25)
flamethrower1.damaged(25)

## 클래스 상속하기 
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{} 유닛을 생성했습니다.".format(self.name))
        print("체력 : {0} 공격력 : {1}".format(self.hp, self.damage))

class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp) # 공통 부분은 부모 클래스의 생성자를 호출해서 가져옴 (변수 또다시 정의하지 않고)
        self.damage = damage

    def attack (self, location):
        print("{0} : {1} 방향 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 만큼 피해를 입었습니다.".format(self.name, damage))
        self.hp -= damage

        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp)) 
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

flamethrower1 = AttackUnit("화염방사병", 50, 16)
flamethrower1.attack("5시")

flamethrower1.damaged(25)
flamethrower1.damaged(25)

## 다중 상속
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly (self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}] ".format(name, location, self.flying_speed))

class FlyableAttackUnit (AttackUnit, Flyable):
    def __init__ (self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

interceptor = FlyableAttackUnit("요격기", 200, 6, 5)
interceptor.fly(interceptor.name, "3시")

class Unit :
    def __init__(self, name, hp, speed):
        self.name = name 
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [ 속도 {2}]".format(self.name,location, self.speed))


class AttackUnit(Unit):
    def __init__ (self, name, hp, damage, speed):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

class FlyableAttackUnit (AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage, 0) #추가된 지상 이동 속도 (speed) = 0으로 정의
        Flyable.__init__(self,flying_speed)

hoberbike = AttackUnit("호버 바이크", 80 ,20, 10)
spacecruiser = FlyableAttackUnit("우주 순양함", 500, 25, 3)

hoberbike.move("11시")
spacecruiser.fly(spacecruiser.name, "9시")

## 메서드 오버라이딩 
class FlyableAttackUnit (AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage, 0) #추가된 지상 이동 속도 (speed) = 0으로 정의
        Flyable.__init__(self,flying_speed)

    def move (self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

hoberbike.move("11시")
spacecruiser.move("9시")

## 동작 없이 일단 넘어가기 : pass
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        Unit.__init__(self, name, hp, 0)
        self.location = location

# 다음과 같이 작성도 가능 (super() 사용 시 self 빼고 전달)
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        super.__init__(name, hp, 0)
        self.location = location

supply_depot = BuildingUnit("보급고", 500, "7시")



#다중 상속일 때 : super () 사용 시 가장 먼저 상속받은 부모 클래스에만 접근 
class Unit :
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Flyable, Unit):
    def __init__(self):
        super().__init__()

troopship = FlyableUnit()

#다중 상속일 때는 다음과 같이 각각 명시 
class Unit :
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Flyable, Unit):
    def __init__(self):
        Flyable.__init__(self)
        Unit.__init__(self)


