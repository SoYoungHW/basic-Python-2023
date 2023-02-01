# 구구단 프로그램
for x in range(2,10):
    print(f'{x}단 시작 =======')
    for y in range(1,10):
        print(f'{x} X {y} = {x*y:>2}', end=' ') # :>2 두자리로 만들어서 정렬
    print() # for y in range(1,10)문에 걸림 / 반복끝나고 출력
    
# 디버깅 - 오류를 잡기위해 만들어짐, 이해가 안될 때도 사용
# 중단점 - 디버깅할때 중단하는 지점
# F10 이동키 / F5 전부 실행

# print() 한줄띄우기
# print('\n') 두줄띄우기