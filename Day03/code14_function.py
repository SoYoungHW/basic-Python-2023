# 함수
# 함수정의(실행이 아님)
def add(x,y):
    result = x + y
    return result

def sub(x,y):
    result = x - y
    return result

def mul(x,y):
    result = x * y
    return result

def div(x,y):
    result = x // y
    return result

# 함수호출
val = add(1024,5)
print(val)

val = sub(1024,1000)
print(val)

val = mul(512,2)
print(val)

val = div(108,10) # 컴퓨터는 0으로 나누기 불가(무한대)
print(val)


# 함수는 호출하면 답을 리턴
# 매개변수=파라미터=인자
# F11 디버깅 함수 이동키
# 정의하는 함수의 순서는 상관없음