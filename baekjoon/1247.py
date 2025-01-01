#N개의 정수가 주어지면, 이 정수들의 합 S의 부호를 구하는 프로그램을 작성하시오.

for i in range(3):
  N = int(input())
  lst = [0]*N

  for i in range(N):
    num = int(input())
    lst[i] = num
    
  sum_lst = sum(lst)
  if sum_lst == 0:
    print(0)
  elif sum_lst>0:
    print("+")
  else:
    print("-")