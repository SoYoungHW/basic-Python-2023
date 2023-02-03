# 외부 패키지를 사용
import requests

res = requests.get('https://www.naver.com')
print(res.status_code)
print('-------------------------')
print(res.content) # 웹사이트 소스를 다 받아옴