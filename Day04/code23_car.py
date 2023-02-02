# 자동차 클래스
class Car:
    __number = '54라 9538' # __ 함부로 변경불가

    def get_number(self) -> str: # -> str 생략가능
        return self.__number

    def set_number(self, number):
        self.__number =number

    def __init__(self, number = '54라 9538') -> None:
        self.__number = number
        print('__init__') # 대개 init 을 생성자라고 함(자주 사용)

    # def __new__(cls): 
    #     print('__new__') # new 가 먼저 시작
    #     return super().__new__(cls) # 부모클래스(상속)(super)

    def __str__(self) -> str:
        return f'차번호는 {self.__number}'

yourcar = Car(number='88호 7486')
print(yourcar)
yourcar.__number = '54라 9999' # 외부에서는 멤버변수에 접근불가
print(yourcar)
print('클래스 내부함수 사용')
yourcar.set_number('55오 5555')
print(yourcar)

mycar = Car()
print(mycar)
print(f'제 차는요, 아이오닉이고 번호가 {mycar.get_number()}(이)에요.') 

mycar.__number = '132거 8874'
print(mycar.get_number())
print(mycar)