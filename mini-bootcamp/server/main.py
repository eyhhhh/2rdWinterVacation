# 웹 서버 만들기
from socket import *

def createServer():
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
          #print(request)
          
          # 고객께 답변 드리기
          response = 'HTTP/1.1 200 OK\n'
          response += 'Content-Type: text/html\n'
          response += '\n' # 여기까지 헤더 규격
          response += '<html><body>Hello World</body></html>\n'
          cSocket.sendall(response.encode('utf-8'))
          
          # 전화 끊기
          cSocket.shutdown(SHUT_WR)
            
    except KeyboardInterrupt:
        print('\nShutting down the server\n')
        serverSocket.close()
        
if __name__ == '__main__':
    createServer()