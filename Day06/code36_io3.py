# 콘솔출력 보충
# 이스케이프 캐릭터(탈출문자)
print('1.Hello.\r\nworld')
print('2.Hello.\nworld') # 이걸 권장합니다

print('3.Hello.\n\tworld') # t 탭
print('4.Hello.\n\t\bworld') # b 백스페이스

print('5.Hello.\n\'world\'') # \' 문자열내 홑따옴표 
print('6.Hello. "world"') 
print('7.Hello. \"world\"')

print('8.Hello.\\ world') # \를 문자열에 표현(파이썬은 하나만 써도 OK)
print('9.Hello\0') # 문자열의 마지막 표현

# 파이썬에서는 쓰지않는게 많으나, C나 자바 등 다른 언어에는 자주 사용

# 문자열 포맷팅 - 구닥다리(자격증 시험에는 나옴)
# %로 포맷코드를 시작
me = '저'
name = '소영'
age = 40
print('%s는 %s입니다. %d대 입니다.' %(me, name, age)) # 순서 바꾸면 안됨

print(f'{254.112233:.2f}') # 최신식 # 소수점 두번째에서 자름
print('%9.2f' %(254.112233)) # 구식 # 전체자리수.소수점