# if문을 배워요
name = '소영'
state = '아픔'

if name == '소영': # '=' 오른쪽값을 대입, '==' 좌우가 같다, '!=' 좌우가 같지 않다 # ':'으로 끝을 알림
    print('진료실에서 담당의사를 만납니다.')
    if state =='아픔': # 중복(다중) if문
        print('선생님, 아파요')
        print('배가 어떻게 아프십니까?') # 들여쓰기 안맞추면 오류
    else:
        print('어디가 아프십니까?')
        print('안 아픈데요')
elif name == '승은': # 또 다른 조건
    print('주사실로 갑니다.')
else:
    print('조용히 기다립니다.') # 참이 아닐 경우 출력