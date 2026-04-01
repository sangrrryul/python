def func_plus(param):
      return param +10

def func_minus(param):
      return param -10

inp = int(input())
#print(inp)
ret1 = func_plus(inp)
ret2 = func_minus(inp)
print(f"{inp} + 10 = {ret1}")
print(f"{inp} - 10 = {ret2}")