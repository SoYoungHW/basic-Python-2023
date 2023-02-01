# 좀 더 복잡한 계산기
def calc(option, *args):
    result = 0
    if option == 'add':
        for i in args:
            result += i

    elif option == 'mul':
        result = 1
        for i in args:
            result *= i

    elif option == 'sub':
        result = args[0] # 첫번째거부터 시작(빼기) / 순서가 바뀌면 안되니까 
        for i in args[1:]:
            result -= i

    elif option == 'div':
        result = args[0] # 첫번째거부터 시작(나누기) / 순서가 바뀌면 안되니까
        for i in args[1:]:
            result /= i

    return result

print(calc('add',5,7,17)) #29
print(calc('mul',512,2,2)) #2048
print(calc('sub',10,248,396)) #-634
print(calc('div',100,5)) #20.0

# 여러 값을 리턴할때는 튜플을 사용
def new_calc(x,y):
    return (x*y, x/y, x+y, x-y)

# 받을때는 튜플(소괄호) 생략가능
res1, res2, res3, res4 = new_calc(5,7)
# (res1, res2, res3, res4) = new_calc(5,7)
print(res1, res2, res3, res4)

# print(type(new_calc(5,7))) 로 클래스를 알아내야함
# 더블클릭하면 다 선택됨     