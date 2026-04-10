N = int(input())
print(N)

for i in range(10, N+1,10):
    print(i)

#----------------------------

N = int(input())
print(N)

for i in range(10, N+1):
    if i%10 == 0:      #몫이 0이 나오게 설정 
     print(i)

#----------------------------

N = int(input())
print(N)

i=10
while i <= N:
    print(i)
    i +=10  