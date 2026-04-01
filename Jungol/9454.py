a,b = map(int,input().split())
#print(a, b)

def func_plus(p1, p2):
    return p1 + p2

ret = func_plus(a,b)
print(ret)

def func_minus(p1, p2):
    ret

#------------------------------

def A(x, y):
    return x + y

def B(x, y):
    return abs(x - y)     #abs 절대값구하는코드

n1, n2 = map(int, input().split())

print(f"두 수의 합 = {A(n1, n2)}")
print(f"두 수의 차 = {B(n1, n2)}")    