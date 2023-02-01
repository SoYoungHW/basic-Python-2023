# 전체/지역변수 
num = 1

for i in range(1,11):
    num = i * num
    print(f'{i + 1}번')

    if i % 3 == 0: # 3의 배수
        res = '테스트'
        print(res)

print(f'결과{num}')
print(res)

# 함수를 안쓸때는 글로벌과 로컬 동일 / 함수를 쓸때 구분