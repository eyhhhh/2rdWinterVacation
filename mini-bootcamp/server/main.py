# 웹 서버 만들기
from socket import *
import json
import re

DB = [
    {'id': 1, 'name': 'Trump'},
    {'id': 2, 'name': 'Biden'},
    {'id': 3, 'name': 'Obama'},
]

def get_user_from_db():
    return DB
 
def parseRequest(requests: str) -> str | None: # 반환형은 str 또는 None
    if len(requests) < 1:
        return None
    
    arRequests = requests.split('\n')
    for line in arRequests:
        match = re.search(r'\b(GET|POST|DELETE|PUT|PATCH)\b\s+(.*?)\s+HTTP/1.1', line) # 정규표현식: req에서 첫줄?만 가져옴
        if match:
            strMethod = match.group(1) # 1번 그룹에 대응되는 값
            print(strMethod)
            strPath = match.group(2) # 2번 그룹에 대응되는 값
            return strPath
    return None

def createServer():
    arPath = ['/','/users','/google.png']
    serverSocket = socket(AF_INET, SOCK_STREAM) # 소캣 만들기
    try:
        serverSocket.bind(('localhost', 8080)) # 포트 선점
        serverSocket.listen()
        while True:
          # 전화 오면 받기
          (cSocket, addr) = serverSocket.accept() # Blocking
          print('Connection received from ', addr) # 고객 전화번호
          
          # 고객 말씀 듣기
          request = cSocket.recv(1024).decode('utf-8') # 요청 크기 제한 : 1024byte
          print(request)
          strPath = parseRequest(request)
          print(f'Path={strPath}')
          
          
          # 고객께 답변 드리기
          response = ''
          if strPath not in arPath:
            response = 'HTTP/1.1 404 Not Found\n'
            response += '\n'
            response += '<html><body>페이지를 찾을 수 없습니다.</body></html>\n'
          elif strPath == '/users':
            users = get_user_from_db()
            response = 'HTTP/1.1 200 OK\n'
            response += 'Content-Type: application/json; utf-8\n'
            response += '\n'
            response += json.dumps(users)
          elif strPath == '/google.png':
              response = 'HTTP/1.1 200 OK\n'
              response += 'Content-Type: image/png\n'
              response += '\n'
              cSocket.sendall(response.encode('utf-8'))
              with open('google.png', 'rb') as f:
                while chunk := f.read(1024):
                    cSocket.sendall(chunk)
              cSocket.shutdown(SHUT_WR)
              continue
          else:
            response = 'HTTP/1.1 200 OK\n'
            response += 'Content-Type: text/html\n'
            response += '\n' # 여기까지 헤더 규격
            response += '<html><body>Hello World<img src="/google.png"></body></html>\n'
            
          cSocket.sendall(response.encode('utf-8')) # 한글이 들어가면 얘를 꼭 해야 문자가 안깨짐  
          
          # 전화 끊기
          cSocket.shutdown(SHUT_WR)
            
    except KeyboardInterrupt:
        print('\nShutting down the server\n')
        serverSocket.close()
        
if __name__ == '__main__':
    createServer()