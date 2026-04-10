class SuperStar:  #변수 이름이 superstar
    K = 0

def GetDiff(n):
    return abs(n - SuperStar.K)

SuperStar.K = int(input())
venus = map(int, input().split())

print(*(GetDiff(x) for x in venus), sep='\n')