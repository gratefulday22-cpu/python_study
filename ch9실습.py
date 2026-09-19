## 부동산 프로그램 만들기

class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)

option1 = House("강남", "아파트", "매매", "10억 원", "2010년")
option2 = House("마포", "오피스텔", "전세", "5억 원", "2007년")
option3 = House("송파", "빌라", "월세", "500/50만 원", "2000년")

print("총 3가지 매물이 있습니다.")
option1. show_detail()
option2. show_detail()
option3. show_detail()

# show_detail 이라는 메서드를 하나만 만들었는데도, 객체명에 따라 호출할 때마다 self가 바뀌므로 서로 다른 집 정보 출력 가능

## 모범답안
class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)


houses = []
house1 = House("강남", "아파트", "매매", "10억 원", "2010년")
house2 = House("마포", "오피스텔", "전세", "5억 원", "2007년")
house3 =House("송파", "빌라", "월세", "500/50만 원", "2000년")

houses.append(house1)
houses.append(house2)
houses.append(house3)

print("총 {0}가지 매물이 있습니다.".format(len(houses))) #houses 리스트에 객체가 몇 개 있는지 확인 
for house in houses:
    house.show_detail()


## 차량 등록 관리 프로그램 작성
class ParkingManager:
    def __init__(self, capacity):
        self.capacity = capacity
        self. count= 0

    def register(self):
    

        if self.count >= self.capacity:
            print("더 이상 등록할 수 없습니다.")

        else:
            print("총 {0}대를 등록할 수 있습니다.".format(self.capacity - self.count))
            self. count += 1
            print("차량 신규 등록 ({0}/{1})".format(self. count,self.capacity))



manager = ParkingManager(5)
for i in range(6):
    manager.register()

    


        

