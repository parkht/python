import numpy as np
import matplotlib.pylab as plt

# np.arange(50) : 0 부터 1씩 증가하여 49까지 데이터 50개를 생성
# np.random.randint(0, 50, 50) : 0 부터 49까지 중 랜덤으로 데이터 50개 생성
# np.random.randn(50) : 표준정상분포 랜덤 데이터 50개 생성
# 분산 : 표준값(평균 등)에서 현재 값이 떨어진 정도 -> 표준값 - 분포값
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
print(data)
# 분포도 * 10(퍼짐) -> 기준값에서 떨어진 정도 : +값은 위에, -값은 아래
data['b'] = data['a'] + 10 * np.random.randn(50)
# d -> 동그라미의 크기 : 항상 +값만 가진다. np.abs() -> 절대값
data['d'] = np.abs(data['d']) * 100

# plt.scatter(x좌표값 키, y좌표값 키, c=컬러키, s=사이즈 키, data = 디셔너리데이터터
plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()
