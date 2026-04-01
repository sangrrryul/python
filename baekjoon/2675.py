T = int(input())    
print(T)            #T = 정수
for x in range(T):         
    R, S = input().split()   # 3 ABC
    #print(R,S)

    for i in S:
        for j in range(R):
        print(i, end='')

#---------------------------------------

T = int(input())

for _ in range(T):
    R, S = input().split()
    R = int(R)

    for x in S:
        print(x*R, end='')
    
    print()








