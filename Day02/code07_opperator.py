# 연산자
# 할당연산 assignment
# 2 = 1 (X)
val = 1

# equal 연산자
print(1 == 1)

# 사칙연산
print(1 + 1)
print(1 - 1)
print(10 * 10)
print(1024 / 2) # 소수나누기
print(1024 // 2) # 정수나누기
print(6 // 3)
print(6 % 3) # 나머지 3=>0 6=>0 9=>0 12=>0

# print(6 / 0) # 이러지마
# print(6 // 0) # 컴퓨터에서는 0으로 나눌 수 없다

print(2 ** 10) # 2의 10승

# 문자열연산(더하기와 곱하기만 존재)
first = 'Hello'
second = 'Would'
print(first + second)
print(first + ' ' + second)
print(first, second)

print(first * 4)

# 문자열 길이
print(len(first))
print(first[0]) # 0부터 시작
print(first[1])
print(first[2])
print(first[3])
print(first[4])
# print(first[5]) # Index 에러

# 파이썬에서 인덱스 찾는 특이한 방법
print(first[-1]) # 뒤에서부터는 -1로 시작
print(first[-2])
print(first[-3])
print(first[-4])
print(first[-5])
# print(first[-6]) # Index 에러

# 리스트 자르기
current = '2023-01-31 15:14:02' # 현재시간
print(len(current))
print(current[0:4])
print(current[5:7])
print(current[8:10])
print(current[11:13])
print(current[14:16])
print(current[17:])

print(current[-19:-15])

# 리스트 연산
que = [1,2,3,4,5]
que[0] = 7

print(que)

que.append(10) # 맨 마지막에 추가
print(que)

que.insert(3,99) # 특정 인덱스에 추가
print(que)

que.remove(99) # 해당 값 삭제
print(que)

# 이런거 안됨
# tup = (1,2,3,4,5) # 튜플은 수정불가
# tup[1] = 9

# print(tup)

# 문자열 == 문자 리스트
title = 'python'
print(title)

# title[0] = 'P' # 문자열에서는 값 변경X
print('P' + title[1:])

# 일반적인 문자형 리스트
text = ['p','y','t','h','o','n']
print(text)
text[0] = 'P'
print(text)

# 문자열 포맷팅
print("I'm so happy {0} you,{1}!!".format(2, 'Hey'))
# 소괄호 안의 내용을 중괄호 안에 넣음

#최신식 문자열 포맷팅
preword = 2
sayHello = 'Hey'
print(f"I'm so happy {preword} you,{sayHello}!!")
# 예) 로그인할때 환영인사 등에 사용

pi = 3.141592
print(f'파이는 {pi}입니다.') 
print(f'파이는 {pi:0.02f}입니다.') # 소수점 두번째자리까지만 출력
print(f'파이는 {pi:10.3f}입니다.')

# 문자열을 특정문자로 자르기
full_name = 'So Young. HW'
vals = full_name.split() # 공백(스페이스)으로 자르기
print(type(vals))
print(vals)

vals = full_name.split('.') # .으로 지정
print(vals)

print(full_name.replace('So', 'Ashely')) # 문자 바꾸기

# 문자열 공백 없애기 # 예) 검색엔진(구글, 네이버...) 등에 사용
hi = '          Hello~ Bye          '
print(hi.lstrip() + '|')
print(hi.rstrip() + '|')
print(hi.strip() + '|')

# 문자열에서 값을 찾기
print(full_name.index('Y')) # 해당 문자가 몇번째에 있는지
# print(full_name.index('Z'))

print(full_name.find('Z')) # 찾는 게 없으면 -1
print(full_name.find('Y'))

# 찾는 단어의 개수
print(full_name.count('o'))

# 모든 단어를 대문자/소문자로 변경 # 검색엔진 등에 사용
print(full_name.upper()) # 대문자
print(full_name.lower()) # 소문자

# 연산자 우선순위
print(3 + 4 * 2)
print((3 + 4) * 2)