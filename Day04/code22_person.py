# 클래스 생성
class Person:
    # pass # 뭐적을지 모를때(오류를 없애기 위해)
    name = '익명' # 속성변수=멤버변수(글로벌)
    height = ''
    gender = ''
    blood_type = 'A'

    # 1. 생성자 추가
    # def __init__(self) -> None:
    #     self.name = '홍길동'
    #     self.height = '170'
    #     self.gender = 'male'
    #     self.blood_type = 'AB'
   
    def __init__(self, name = '홍길동', height = 170, gender = 'male') -> None: # 매개변수(로컬-연한글씨)
        self.name = name
        self.height = height
        self.gender = gender

    def walk(self): # self 가 빠지면 작동하지 않음
        print(f'{self.name}이(가) 걷습니다.')
    
    def run(self, option):
        if option == 'Fast':
            self.walk()
            print(f'{self.name}이(가) 빨리 뜁니다.')
        else:
            print(f'{self.name}이(가) 천천히 뜁니다.')

    def stop():
        print(f'{self.name}이(가) 멈춥니다.')

    # 2. 생성자 외 매직메서드(펑션) __str__
    def __str__(self) -> str:
         return f'출력 : 이름은 {self.name}, 성별은 {self.gender}'


SoYoung = Person('소영',157,'female') # 객체 생성 # 객체를 instance 라 부름
# SoYoung.name = '소영' # 이름을 지정해주지 않으면 다 홍길동으로 출력됨(1.생성자추가에서)
# SoYoung.height = '157'
# SoYoung.gender = 'female'
# SoYoung.blood_type = 'O'
# 정육면체 파란색 - 속성변수
# 정육면체 보라색 - 함수

print(f'{SoYoung.name}의 혈액형은 {SoYoung.blood_type} 입니다.')

SoYoung.run('Fast')
print(SoYoung)

# 초기화 후 객체생성
hong = Person()
hong.run('Slow')
print(hong)

print('----------------------------------------')
# 2. 파라미터를 받는 생성자를 실행
ashely = Person('애슐리',165,'female')
print(ashely.name)
print(ashely.height)
print(ashely.gender)
print(ashely)