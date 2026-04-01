#두 명의 이름, 나이를 입력받아 18세 이상이면 adult, 아니면 child라고 정의.
#출력예와 같이 출력하는 프로그램 작성하시오.

#출력값 Alex(11) : child
#      Brown(56) : adult
# ----------------------------------------------------------------------

class Man():
    def __init__(self,name,age):
       self.name = name
       self.age = int(age)

people =[]

def print(self):
        result = 'child'
        if self.age >= 18:
            result = 'adult'
        else:
            result = 'child'

        print(f"{self.name}({self.age}) : {result}")   

for x in range(2):
    name, age = input().split()      

name, age = input().split()
print(name, age)

m1= Man(name, age)
m1.Info()

for _ in range(2):
    n, a = input().split()
    # print(n, a)
    people.append(Person(n, a))

for p in people:
    category = "adult" if p.age >= 18 else "child"
    print(f"{p.name}({p.age}) : {category}")