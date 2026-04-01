num = []    #num 리스트화

for i in range(30):
    print(int(input()), end=' ')

#강사님------------------------
lst =[]

for i in range(30):
    lst.append(int(input()))

#print("----")
for i in lst:
    print(i, end=' ')

#--------------------------------
numbers = [int(input()) for _ in range(30)]  #리스트컴프리헨션 - 입력을 30번 받아서 리스트로 만들어라는 뜻.
print(*numbers)



    


