# 자료형
# None 값이 없는 값
None # 컴퓨터왈 난몰라

print(None)
print(0 == None)
print('' == None)

# 숫자형
val = 3
print(type(val))

val = 3.14
print(type(val))

val = 'Hello'
print(type(val))

val = 0b1010
print(type(val))

val = 12.456548486548786975454876332184
print(type(val))

val = 4_520_000
print(val)

val = 3_099.99
print(val)

# 문자열
val = 'Life is short, You need Python.'
print(val)
print(type(val))

val = 'Hell\nWould!' # 탈출문자 # 한줄띄우기
print(val)
val = 'Hell\tWould!' # 네칸띄우기
print(val)
val = 'Hell\t\bWould!' # 세칸띄우기
print(val)

val = '''Life is short,
You need Python'''
print(val)
val = "Hi, I'm 'So'"
print(val)
val = 'Hi, I\'m \'So\''
print(val)

# 불린형 or 불형
참 = True
거짓 = False
print(type(거짓))

print(1 + 1 == 2)
# 거짓이라는 False 값 변수가 참이냐
print(거짓 == True)
print(거짓 == False)
print(거짓 is False)

print(bool(1)) # 1 == Ture
print(bool(0)) # 0 == False
print(bool(3)) # 1이외의 값은 True라고 하지마세요