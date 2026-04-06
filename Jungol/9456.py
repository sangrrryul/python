# 문제 : 함수 f(x)는 ax^2 + bx + c 와 같이 2차 방정식의 결과를 반환하는 함수이다. 
# 세 정수를 입력받은 후, x의 값 2, 3, 5를 각각 전달하여 함수를 실행하여 얻은 결과 f(2), f(3), f(5)의 값을 출력하는 코드 제출.
#--------------------------------------------------------------------------

a, b, c= map(int,input().split())
print(a, b, c)

def f(x, a, b, c):
   return a * x**2 + b * x + c

print(f(2, a, b, c))
print(f(3, a, b, c))
print(f(5, a, b, c))

#----------------------------
def func(x, a, b, c):
    res = a*x*x + b*x + c
    return res

print(f(2, a, b, c))
print(f(3, a, b, c))
print(f(5, a, b, c))    

#-----------------------------
def ElonMusk(x, a, b, c):
    return a * (x**2) + b * x + c

a, b, c = map(int, input().split())
# print(a, b, c)
for x in [2, 3, 5]:  #반복문 필요없이, 이미 리스트에 입력될 값이 정해진 경우. range 필요X
    print(ElonMusk(x, a, b, c))

