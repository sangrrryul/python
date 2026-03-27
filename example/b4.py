a, b, c = map(int, input().split())
print(a,b,c)

s = a + b + c
avg = s // 3
print(s, avg)

print("sum =", s)
print("avg =", avg)

a,b,c = input().split()
print(a,b,c)
s=a+b+c
print(s)

a, b, c = input().split()
#print(a, b, c)
ia = int(a)
ib = int(b)
ic = int(c)
sum = ia + ib + ic
print('sum =', sum)
print('avg =', sum // 3)


nums = [int(input()) for _ in range(7)]

ops = [
    lambda x: x + 2,
    lambda x: x - 2,
    lambda x: x * 2,
    lambda x: x / 2,
    lambda x: x // 2,
    lambda x: x % 2,
    lambda x: x ** 2
]

for i in range(7):
    print(ops[i](nums[i]))
