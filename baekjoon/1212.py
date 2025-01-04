num = input()
result = []

for i in num:
  lst = ['0','0','0']
  n = int(i)
  j = 0
  while(n>0):
    lst[j] = str(n%2)
    n //= 2
    j += 1
  result += lst[::-1]
    
if result[0] == '0':
  result = result[1:]

print(int(''.join(result)))
    

