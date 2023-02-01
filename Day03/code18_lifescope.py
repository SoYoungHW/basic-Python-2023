# 라이프 스코프
a = 1 # 전역변수(글로벌a)

def vartest(x): # 지역변수(로컬a)
    global a # 전역(글로벌)에 있는 함수를 지역(로컬)에서 가져다 쓰겠다
    a = a + x + 1   # 함수안에서만 살아있음 / 나가면 사망
    return a

a = vartest(a)
print(a)
