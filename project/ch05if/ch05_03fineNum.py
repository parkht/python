import random

# 랜덤으로 발생된 숫자 10개를 저장하는 리스트
numbers = []

# range(시작번호, 끝번호+1)
for num in range(0,10):  # 0부터 9까지 반복 마지막 10은 반복 안된다.
    print(num)

    # randrange(발생 시작 숫자, 발생끝숫자+1)
    numbers.append(random.randrange(0,10))
    # 0부터 9까지 랜덤 마지막 10은 랜덤에 포함 안된다.

    print('numbers ->', numbers)

# 0~9 사이의 각각의 데이터가 있는지 없는지 확인
for num in range(0,10):
    if num in numbers:
        print('숫자 %d는 포함되어 있다' % num)
    if num not in numbers:
        print('숫자 %d은 포함되어 있지 않다' % num)






