lst = []                      #숫자 담을 통(리스트)준비!
for x in range(9):
    lst.append(int(input()))  #9번 반복하면서 리스트에 추가. append-리스트에 값 추가

for i in lst:                 #리스트 안의 값을 하나씩 꺼냄. i=1, i=2, i=3...
    print(i, end=' ')      #줄바꿈 대신 공백으로 이어서 출력 
    
#print('\nsum : ', sum(lst))  #리스트 전체 합 출력(확인용)

nsum = sum(lst)    #전체합 저장
fakei = 0            #가짜 난쟁이 인덱스 저장
fakej = 0

for i in range(9):
    for j in range(9):      #모든 조합 확인
        if i==j:
            continue
        nsum -= (int(lst[i]) + int(lst[j]))
        # print(lst[i], lst[j], nsum)
        if nsum == 100:           #합이 "100"
            reali = i
            realj = j
            break
        nsum += (int(lst[i]) + int(lst[j]))

# print(reali, realj)

for i in range(len(lst)):
    if i==reali or i==realj:
        continue
    print(lst[i])      












    