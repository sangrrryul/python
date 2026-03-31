X = int(input())
N = int(input())
print(X)
print(N)
prod=0
for i in range(N):
    a, b = map(int, input().split())
    print(a,b)
    prod += (a*b)

print(prod)

if X ==prod:
   print("Yes")
else:
    print("No")
