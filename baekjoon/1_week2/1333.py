N,L,D = map(int,input().split())

# 노래가 쉬는 구간을 만들고, 
# D의 배수를 검사해서 범위안에 있는지 확인

rest_time = []
check_time = []
total = (L+5)*(N-1) + L

for i in range(0,N): # N-1번 쉴 것 0 1 2
  rest = [x for x in range(L+(i*(L+5)), L+(i*(L+5))+5)]
  rest_time += rest

idx = 1
while True:
  time = idx*D
  check_time.append(time)
  idx += 1
  if time>total:
    break
  
check = False
for t in check_time:
  if t in rest_time:
    print(t)
    check = True
    break
  
if not check:
  for k in check_time:
    if k>total:
      print(k)
      check = True
      break