# 예외처리
def add(a,b):
    return a + b

def mul(a,b):
    return a * b

def div(a,b):
    return a / b

try: 
    x,y = input('두 수를 입력하세요 > ').split()
    x = int(x)
    y = int(y)
except Exception as e:
    print(e)
    exit()
finally:
    print('계속되나요?') # 이거 실행 후 종료됨

# 원시적인 예외처리
# if y == 0:
#     print('y에 0를 넣지마세요')
#     exit()

print('계산 테스트')
try:
    print(div(x,y)) # 0으로 나누기 *예외*
except ZeroDivisionError as e:
    print('0으로 나누면 안돼요')
except Exception as e:
    print(e) # except없으면 오류
    # 예외처리 중 제일 마지막 위치(이거 하나만 써도 무방)
finally:
    print('계산은 계속됩니다.')




print(add(x,y))
print(mul(x,y))
