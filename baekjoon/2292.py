#위의 그림과 같이 육각형으로 이루어진 벌집이 있다. 
#중앙의 방 1부터 시작해서 이웃하는 방에 돌아가면서
#1씩 증가하는 번호를 주소로 매길 수 있다. 숫자 N이 주어졌을 때, 
#벌집의 중앙 1에서 N번 방까지 최소 개수의 방을 지나서 갈 때 몇 개의 방을 
#지나가는지(시작과 끝을 포함하여)를 계산하는 프로그램을 작성하시오. 
#예를 들면, 13까지는 3개, 58까지는 5개를 지난다.







N = int(input())
#print(N)
boundary = 1
x=0

while True:
    if N <= boundary:
        break;
    boundary = boundary +(6*x)
    x = x + 1
    #print(x, boundary)

    print(x)

# --------------------------------------
n=int(input())

i=1
p=1
while i<n:
    i+=6*p
    p+=1
print(int(p))

#-----------------------------------------
class Honeycomb:
    def __init__(self):
        self.layer = 1
        self.max_room = 1

    def expand(self):
        self.max_room += 6 * self.layer
        self.layer += 1

    def find_dist(self, target):
        while target > self.max_room:
            self.expand()
        return self.layer

h = Honeycomb()
print(h.find_dist(int(input())))



