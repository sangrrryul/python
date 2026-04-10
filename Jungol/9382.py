# 문자열 A를 "apple orange banana" 로 초기화하고 단어를 공백으로 구분하여 뒤집어서 마지막 단어부터 출력하고
# 문자열 B를 "   Hello world!   "로 초기화하여
# 출력한 후 앞뒤 공백을 제거한 후 다시 출력하는 프로그램을 작성하시오.


A = 'apple orange banana'
B = '   Hello world!   '

# print(A[::-1]) : 문자 자체를 뒤집어서 출력 .
ra= A.split()
#print(ra)

idx = len(ra)
#print(ra)

for x in len(ra):
    print(ra[x], end=' ')

print()
print(B)
print(B.strip())

# ---------------------------------

A = "apple orange banana"
words = A.split()[::-1]
print(*words)

B = "   Hello world!   "
print(B)
print(B.strip())

# -----------------------------------------------

a='apple orange banana'
b='   Hello world!   '

print(' '.join(reversed(a.split())))
print(b)
print(b.strip())
