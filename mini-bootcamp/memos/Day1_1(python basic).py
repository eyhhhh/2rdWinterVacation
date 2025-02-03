#Pagination
#list의 슬라이싱 기능 사용   

#함수 인자의 기본값 설정(num: int), 또는 타입 캐스팅으로
#Type을 명시하자!!
  
db = ['Linux', 'Windows', 'macOs', 'ubuntu', 'redhat']
def get_product(page: int=1, per_page: int=2) -> list: #반환값은 list
  startIndex = (page-1) * per_page
  endIndex = startIndex + per_page
  return db[startIndex:endIndex]

#Class는 기능 구현, dataclass는 데이터틀로 사용(c언어에서 구조체 느낌낌)
from dataclasses import dataclass

@dataclass
class User:
  loginId: str
  name: str
  age: int
  email: str

def create_user(user: User): #인자를 간단하게 받아올 수 있음
  pass

#입력값은 꼭 검증하기! 프론트를 믿지마라 언제든 오류 발생 가능
#함수 반환값에 None 타입 추가하기 - 예외처리 => list|None / typing 모듈