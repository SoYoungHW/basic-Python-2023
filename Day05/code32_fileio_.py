# 글자 인코딩
# ASCII -> 한단어를 표현하는 체계(영어), 기본
# Unicode(UTF-8) -> 모든 나라언어를 다 

# 파일 만들기

# file = open('C:/DEV/Temp/Bank/sample04.txt', 'w', encoding = 'UTF-8') # 파일 쓰기로 만듦
# a - 추가로 계속 적음 / w - 이전글 지워짐

file = open('../sample07.txt', 'w', encoding = 'UTF-8')
# . 나자신 / .. 부모폴더

file.write('안녕하세요\n')
file.write('두번째 파일이다\n')
file.write('절대경로에 파일이 생성될겁니다.\n')

file.close()
print('sample01,txt가 생성되었습니다')

# 파일/폴더 경로 - 절대경로/상대경로
