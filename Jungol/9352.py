# 50개의 정수를 입력받아 거꾸로 출력.

lst=[]

for x in range(50):
    i = input()
    lst.append(i)

# print(lst)

# print(len(lst))
# print(lst[0])
# print(lst[len(lst)-1]
for i in range(len(lst)-1, -1, -1):
     print(lst[i], end=' ')

#--------------------------------------
lst =[]
for i in range(5):
    lst.append(int(input()))
print(*lst[::-1])