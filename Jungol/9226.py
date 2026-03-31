# a = int(input())
# b = int(input())

# if a>b:
#    a, b = b, a 
#    print(a, b)

# print(a, b)

#1---------------------------
a,b = map(int, input().split())

if a < b:
   print(a)
   print(b)
else:
   print(b)
   print(a)