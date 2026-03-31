N,M = map(int,input().split())
print(N,M)

for n in range(N):
    print("Hello")

print()  # 한 줄 띄우기

for i in range(M):
    print("Hello")

#1-----------------------------------------
def hello():
    print("Hello")

N,M = map(int, input().split())
#print(N,M)

for i in range(N):
    hello()

print()   
 # 한 줄 띄우기
for i in range(M):  
    #print("Hello"*M)
    hello()
