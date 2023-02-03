# 파일 읽어오기
file = open('./Day05/sample05.txt', 'r', encoding='utf-8')

while True:
    text = file.read()
    if not text : break
    
    print(text)

file.close() # 파일/데이터베이스/네트워크 등을 open 하면 반드시 close 해야함!

