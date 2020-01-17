# 0xff(16진수)를 10진수로 -> 255
a = 0xff
# 0o77(8진수)를 10진수로 -> 63
b = 0o77
# 0b1111(2진수)를 10진수로 -> 15
c = 0b1111
# 보여지는건 10진수로 나타내어 진다.
print(a, b, c)

# 변수 a의 타입을 출력해보자
print(a, "의 타입은 ", type(a))

d = 3.14
# 3.14e5 = 3.14 * 100,000 = 314,000.0
e = 3.14e5

print(d, e)
print(d, "의 타입은 ", type(d))

# 2개의 처리문을 한줄에 사용하기 위해서는 ';'으로 구분한다.
a = 10; b = 20
print(a+b, a-b, a*b, a/b)

a, b = 10, 20
print(10 ** 30)

b = 3
print(a/b)
print(int(a/b))
print(a % b)
print(a // b)

# python에서는 True, java에서는 true, R에서는 TRUE 적용 프로그램마다 작성 방식이 다르다
a = True
b = False

print(a, type(a))

# a = 100 == 100 가능 대입과 비교중 우선순위가 비교가 높다, 보기도 어렵다
a = (100==100)

print(a, type(a))

a = "파이썬 만세"
a
print(a)
