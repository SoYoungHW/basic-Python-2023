# random 모듈 사용
import random

# print(random.choice(range(1,7)))
numbers = [i for i in range(1,46)] # 1~45 리스트
lottery = []

for i in range(6): # 6개의 숫자를 고름 
    lottery.append(random.choice(numbers)) # numbers 중에서

print(lottery)