# 다중입력 
# x, y = input('두 영단어를 입력하세요. > ').split()
# print(x)
# print(y)

# 완전 다중입력(갯수가 몇개든지 상관없음)
# 중요!!!!
inputs = list(map(str, input('단어를 입력하세요 > ').split()))
# map : 들어오는 값들을 나열

print(inputs)

inputs = list(map(int, input('정수를 입력하세요 > ').split()))

print(inputs)