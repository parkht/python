import numpy as np
import matplotlib.pylab as plt

#   np.arange(시작값, 종료값(포함하지 않음), 증감값) -> 리스트 데이터를 만든다.
t = np.arange(0., 5., 0.2)

print(t)

# 3개의 데이터를 한꺼번에 넣어서 그래프로 표시되도록 세팅
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^-')
plt.show()