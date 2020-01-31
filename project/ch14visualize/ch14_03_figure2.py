import matplotlib.pylab as plt
import numpy as np

t = np.arange(0, 5, 0.1)

plt.figure(figsize=(8,9))
# subplot 위치 및 데이터 세팅
# np.sqrt() -> 루트값을 구하는 함수
plt.subplot(511).plot(t,np.sqrt(t))
# 위치에 세팅
plt.grid()

plt.subplot(523).bar([1,2,3,4,5],[1,5,3,2,4])
# t**2 -> t의 제곱값
plt.subplot(524).plot(t, t**2)
plt.grid()
# np.sin() -> sin 값
plt.subplot(513).plot(t, np.sin(t))
# np.cos() -> cos 값
plt.grid()
plt.subplot(514).plot(t, np.cos(t))
plt.grid()

plt.subplot(515).plot(t, np.tan(t))
plt.grid()

plt.show()
