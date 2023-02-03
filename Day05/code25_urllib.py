# urllib 패키지 불러오기
from urllib.request import Request, urlopen

req = Request('https://www.naver.com') # 객체 생성
res = urlopen(req) 
print(res.status) # http 코드 200
