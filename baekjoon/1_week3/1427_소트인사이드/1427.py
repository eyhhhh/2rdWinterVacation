num = int(input())

lst = []

while(num>0):
  digit = num%10
  num //= 10
  lst.append(digit)
  
lst.sort(reverse=True)
result = 0
for i in lst:
  result = result*10 + i
print(result)