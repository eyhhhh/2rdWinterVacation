import sys
input = sys.stdin.readline

N = int(input())
lst = ['0']*N

for i in range(N):
  lst[i] = input().strip()
  
names = []
cnt = {}

for i in range(N):
  name = lst[i][0]
  if name in names:
    cnt[name] += 1
  else:
    names.append(name)
    cnt[name] = 1

ncheck = True
result = []
for name in names:
  if cnt[name] >= 5:
    result.append(name)
    ncheck = False

if ncheck:
  print("PREDAJA")
else:
  result.sort()
  print(''.join(result))