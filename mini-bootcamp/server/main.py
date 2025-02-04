from enum import Enum
from socket import *
import re
import json
from dataclasses import dataclass

class HttpContentType(Enum):
    TEXT_HTML = 'text/html'
    APPLICATION_JSON = 'application/json'
    IMAGE_PNG = 'image/png'

class HTTPMethod(Enum):
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'
    PATCH = 'PATCH'

class HTTPStatusCode(Enum):
    OK = (200, 'OK')
    NOT_FOUND = (404, 'Not Found')
    METHOD_NOT_ALLOWED = (405, 'Method Not Allowed')
    MOVED = (301, 'Moved Permanently')
    SERVER_ERROR = (500, 'Internal Server Error')

@dataclass
class HTTPRequest:
    method: HTTPMethod
    url: str
    userAgent: str

DB = [
    {'id': 1, 'name': 'Trump'},
    {'id': 2, 'name': 'Biden'},
    {'id': 3, 'name': 'Obama'}
]

def makeRespHeader(status: HTTPStatusCode, 
                   contentType:HttpContentType,
                   extra: dict|None = None) -> str:
    resp = f'HTTP/1.1 {status.value[0]} {status.value[1]}\n'
    resp += f'Content-Type: {contentType.value}\n'
    if extra is not None:
        for k, v in extra.items():
            resp += f'{k}: {v}\n'
    resp += '\n'
    return resp

def get_user_from_db():
    return DB


def parseRequest(requests: str) -> HTTPRequest | None:
    if len(requests) < 1:
        return None
    
    arRequests = requests.split('\n')
    for line in arRequests:
        match = re.search(r'\b(GET|POST|DELETE|PUT|PATCH)\b\s+(.*?)\s+HTTP/1.1', line)
        if match:
            req = HTTPRequest()
            try:
                req.method = HTTPMethod(match.group(1))
                req.url = match.group(2)
            except:
                return None
            
            return req
    return None

def handle_req(req: HTTPRequest) -> bytes:
    arPath = ['/', '/users', '/google.png', '/google']
    if req is None:
        resp = makeRespHeader(HTTPStatusCode.METHOD_NOT_ALLOWED, 
                                HttpContentType.TEXT_HTML)
        return resp.encode('utf-8')

    print(f'Path={req.url}')
    strPath = req.url
    # 고객께 답변 드리기
    bResp = bytes()
    if strPath not in arPath:
        resp = makeRespHeader(HTTPStatusCode.NOT_FOUND, 
                                HttpContentType.TEXT_HTML)
        resp += '<html><body>없습니다</body></html>\n'
        bResp = resp.encode('utf-8')

    elif strPath == '/users':
        resp = makeRespHeader(HTTPStatusCode.OK, 
                                HttpContentType.APPLICATION_JSON)
        resp += json.dumps(get_user_from_db())
        bResp = resp.encode('utf-8')

    elif strPath == '/google':
        resp = makeRespHeader(HTTPStatusCode.MOVED, 
                                HttpContentType.TEXT_HTML, 
                                {'Location': 'https://www.google.com'})
        bResp = resp.encode('utf-8')
        
    elif strPath == '/google.png':
        resp = makeRespHeader(HTTPStatusCode.OK,
                                HttpContentType.IMAGE_PNG)
        bResp = resp.encode('utf-8')

        with open('google.png', 'rb') as f:
            bResp += f.read()
    else:
        resp = makeRespHeader(HTTPStatusCode.OK, HttpContentType.TEXT_HTML)
        resp += '<html><body>Hello <img src="/google.png" /></body></html>'
        bResp = resp.encode('utf-8')
        
    return bResp

def createServer():
    serverSocket = socket(AF_INET, SOCK_STREAM)
    try:
        serverSocket.bind(('localhost', 8080))
        serverSocket.listen()
        while True:
            # 전화가 오면 받기
            (cSocket, addr) = serverSocket.accept()
            print(addr)
            
            # 고객 말씀 듣기
            req = cSocket.recv(1024).decode('utf-8')
            print(req)
            httpReq = parseRequest(req)

            # 고객님 원하시는 답변 만들기
            bResp = handle_req(req)
            cSocket.sendall(bResp)
            
            # 전화 끊기
            cSocket.shutdown(SHUT_WR)

    except KeyboardInterrupt:
        serverSocket.close()

if __name__ == '__main__':
    # createServer()
    resp = makeRespHeader(HTTPStatusCode.OK, 
                          HttpContentType.TEXT_HTML)
    print(resp)

    print('=' * 20)

    ext = {
        'Location': 'https://www.google.com'
    }
    resp = makeRespHeader(HTTPStatusCode.MOVED,
                          HttpContentType.TEXT_HTML,
                          ext)
    print(resp)