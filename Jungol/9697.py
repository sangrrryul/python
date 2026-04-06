class Player:
    def __init__(self,name,AB,H):  #a = 타수/ b = 안타수
        self.name = name
        self.AB = AB
        self.h = h

    def print(self):
        print(f"name:{self.name}, AVG:{self.getAVG}, AB:{self.ab}")

    def getAB(self):
        return int(self.h)/int(self.ab)

for i in range(2): #-------------------숫자 2의 자리에는 비교할 대상의 숫자로 변경가능. 3~~
    name, ab, h = input().split()
    print(name, AB, H)

AB, H = map(int,input().split())
result = H / AB
print(f"{result:.3f}")











# Betts 58 23    Mikes 59 22
# name:Betts, AVG:0.397, AB:58, H:23
# name:Mikes, AVG:0.373, AB:59, H:22