"집이 위치한 도시, 방의 수, 화장실의 수를 입력받아 출력예와 같이 출력하는 프로그램을 작성하시오."

"출력답"
location: Chico
bedrooms: 4
bathrooms: 2

#1--------------------------------------------------------------------

class House():
     def __init__(self,loca, bed, bath):
             self.loca = loca
             self.bed = bed 
             self.bath = bath
     def print(self):
         #print(loca, bed, bath)
         print("location:", loca)
         print("bedrooms:", bed )
         print("bathrooms:", bath)

loca, bed, bath = input().split()
#print(loca, bed, bath)

h1 = House(loca, bed, bath)
h1. print() 

#2---------------------------------------------------------------
class House:
    def __init__(self, location, bedrooms, bathrooms):
        self.location = location
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms

    def show_info(self):
        print(f"location: {self.location}")
        print(f"bedrooms: {self.bedrooms}")
        print(f"bathrooms: {self.bathrooms}")

data = input().split()
my_house = House(data[0], data[1], data[2])
my_house.show_info()

