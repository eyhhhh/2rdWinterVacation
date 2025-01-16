N = int(input())

result = []
num = 666

while len(result)<=N:
  if '666' in str(num):
    result.append(num)
  num += 1
  
print(result[N-1])

