import sys
input = sys.stdin.readline

cnt = 1
while True:
    n = int(input()) # 참여 학생 수
    if n == 0: # 종료 조건
      break
    
    peoples = [] # 학생 입력
    for i in range(n):
      data = input().split()
      peoples.append(data)
    
    result = []
    for i in range(n):
      name = peoples[i][0] #학생 이름
      msg = peoples[i][1:] #메세지들

      for j in range(n-1):
        m = msg[j]
        if m == "N":
          result.append([peoples[(i-j-1+n)%n][0],name])
      
    if cnt!=1 :
      print("")
      
    print(f"Group {cnt}")
    if len(result) == 0:
      print("Nobody was nasty")
    else:
      for r in result:
        print(f"{r[0]} was nasty about {r[1]}")
     
    cnt += 1