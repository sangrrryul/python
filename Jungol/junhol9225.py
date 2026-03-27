# n1 = int(input) 
# n2 = int(input)
# print(n1,n2)
# print(n1 +n2)

# N, M = map(int, input().split())
# print(N, M)
# print(N + M)

# if N % 2 == 1 or M % 2 == 1:
#     print("ODD")

N=int(input())
M=int(input())
print(N)
print(M) 
print(N + M)    

if N % 2 == 1:
    print('ODD')
else:
    print('짝수')    

#1------------------------------------------
#강사님ver.

N = int(input())
M = int(input())
# print(N)
# print(M)
print(N + M)

if N % 2 == 1:
    print('ODD')
else:
    if M % 2 == 1:
        print('ODD')
