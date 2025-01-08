import sys
input = sys.stdin.readline

def fac(n):
  if n == 1 or n == 0:
    return 1
  else:
    return n*fac(n-1)

# 조합(nCr)공식 사용 : r개중 n개를 순서대로 선택
def MakeCase(n,m):
  return int(fac(m)/ (fac(n)*fac(m-n)))
  
T = int(input())
sights = [0]*T

for i in range(T):
  sights[i] = input().split()

for s in sights:
  total = 0
  N, M = int(s[0]), int(s[1])
  total += MakeCase(N,M)
  print(total)