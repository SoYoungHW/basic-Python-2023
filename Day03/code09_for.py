# for문
arr = [1,2,3,4,5]
sum = 0

for item in arr: # 순차적으로 반복 후 빠져나감
    print(item)
    sum += item # sum = sum + item

print('합계는', sum) # 띄워서 for구문과 구분

# 리스트를 편하게 만드는 방법
vals = [i for i in range(1,11)] # 10까지 적으면 9까지 출력됨, 컴퓨터는 0부터 시작하니까
print(vals)

# continue / break # 반복문에만 사용(if문에 사용불가)
num = 0
for item in vals:
    num += 1 # num = num + 1 # 1씩 추가시킴
    if num % 2 == 0: # 짝수
        # continue # 이후의 것을 수행하지 않고 다시 for문으로 감
        break # break만나면 for문을 완전히 탈출
    else:
        print(num, '번 수는', item, '입니다')

print(range(0,10)) # 범위를 0부터 9까지 만듦


