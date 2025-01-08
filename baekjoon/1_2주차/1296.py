import sys
input = sys.stdin.readline

yeondu = input().strip()
N = int(input())

teams = [0]*N
values = {}

for i in range(N):
  team = input().strip()
  teams[i] = team
  
teams.sort()
for t in teams:
  value = t + yeondu
  l,o,v,e = value.count('L'), value.count('O'), value.count('V'), value.count('E')
  values[t] = [l+o, l+v, l+e, o+v, o+e, v+e]

best = -1
for t in teams:
  result = 1
  for i in range(6):
    result *= values[t][i]

  result %= 100
  if best < result:
    best = result
    bestName = t
    
print(bestName)