# 함수
# 함수정의(실행이 아님)
# 함수만드는 방법 4가지
  #1. 파라미터O 리턴O
  #2. 파라미터O 리턴X
  #3. 파라미터X 리턴O
  #4. 파라미터X 리턴X
def add(x,y):
    result = x + y
    print(result)
    return # 생략가능
    
def sub(x,y):
    result = x - y
    print(result)
    
def mul(x,y):
    result = x * y
    print(result)
    
def div(x,y):
    result = x // y
    print(result)

def hello():
    print('Hello~')
    
def hello2():
    msg = 'Hello, Hello'
    return msg

# 함수호출
hello()
print(hello2())

add(1024,5)
sub(1024,1000)
mul(512,2)
div(108,10) # 컴퓨터는 0으로 나누기 불가(무한대)
