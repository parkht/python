# print(형식문자열 % 데이터) - 출력 후 줄바꿈을 한다.
# %d - 정수형 데이터
print('%d입니다.' % 123)
print('%5d입니다.' % 123)
print('%05d입니다.' % 123)

# %f - 실수형 데이터
print('%f입니다' % 123)
# print('%전체자리수.소수점이하f - 기본은 반올림한다.' % 숫자)
print('%7.1f입니다' % 123.41)
print('%7.1f입니다' % 123.45)
print('%07.1f입니다' % 123)
print('%7.3f입니다' % 123.45)
print('%6.3f입니다' % 123.45)
print('%5.3f입니다' % 123.45)

print('%s' % 'python')
print('%8s' % 'python')

print('%d %5d %05d' % (123,123,123))
print('{0:d} {1:5d} {2:05d}'.format(123, 456, 789))
print('{2:d} {1:5d} {0:05d}'.format(123, 456, 789))

print("한 행입니다. 또 한 행입니다.")
print("한 행입니다. \n 또 한 행입니다.")

a = 100.5234
print(int(a))

a=2
print(a)
print(float(a))

a="two"
print(a)

var4=var3=var2=var1=100
print(var1)
print(var2)
print(var3)
print(var4)