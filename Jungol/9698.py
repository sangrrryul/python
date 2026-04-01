class Building():
    def __init__(self,year,price):
            self.year = int(year)
            self.price = int(price)

    def print(self):
        print(self.year, self.price)

N=int(input())
#print(N)     #건물 개수 입력 '4'입력
                                     #Y-year/ P-price
buildings=[]  #건물 목록 리스트화

for _ in range(N):
    Y, P = map(int, input().split())
    #print(Y, P)
    building.append(Building)

#-----------------------------------------

N = int(input())  # 건물 개수

buildings = []  # 리스트

# 건물 정보 입력
for _ in range(N):
    year, price = input().split()
    buildings.append(Building(year, price))

# 기준 입력
Y, P = map(int, input().split())

# 조건에 맞는 건물 출력
for b in buildings:
    if b.year >= Y and b.price <= P:
        b.show()

#------------------------------------------
#강사님 코드
class Building:
    def __init__(self, year, price):
        self.year = year
        self.price = price
    def print(self):
        print(self.year, self.price)

build = []

N = int(input())
for i in range(N):
    year, price = map(int,input().split())
    b = Building(year, price)
    build.append(b)

#print("---")

for j in build:
    build[j].print_building()

Y, P = map(int, input().split())
#print(Y, P)

for k in range(N):
    if build[k].year >= Y and build[k].price <= P:
       build[k].print_building()