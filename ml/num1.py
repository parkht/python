import numpy as np
# 생성 np.array(리스트, 속성) 속성 : dtype
# a = [1, 2, 3, 4, 5]
# print(type(a))  # <class 'list'>
# arr1 = np.array(a)
# print(arr1)  # [1 2 3 4 5]
# print(type(arr1))  # <class 'numpy.ndarray'>
# arr1 = np.array(a, dtype=float)
# print(arr1)  # [1. 2. 3. 4. 5.]
# 2차원 배열
# b = [[1, 2, 3], [4, 5, 6]]
# arr2 = np.array(b)
# print(arr2)
# [[1 2 3]
#  [4 5 6]]
# 3 차원 배열
# c = [[[1, 2],[3, 4]],[[5, 6],[7, 8]]]
# arr3 = np.array(c)
# print(arr3)
# [[[1 2]
#   [3 4]]
#
#  [[5 6]
#   [7 8]]]
# print(arr3.shape)  # (2, 2, 2)
# print(arr3.dtype)  # int32
# print(arr3.ndim)  # 3
# a = [1, 2, 3, 4, 5]
# arr1 = np.array(a)
# print(arr1.shape)
# ------------------------------------------------------------
# 초기화 함수
# np.zeros(shape, 속성) -> 0으로 채워라
# np.ones(shape, 속성) -> 1로 채워라
# np.full(shape, 속성) -> 9로 채워라
# np.empty(shape, 속성) -> 남아있는 메모리 값으로 채워라
# np.eye(숫자, 속성)  -> 숫자는 (a, a) 행과 열의 숫자가 같은것을 나타낸다
# x = np.zeros((2, 4))
# print(x.dtype)  # float64
# x = np.zeros((2, 3, 4), dtype=int)
# print(x.dtype)  # int32
# x = np.full((5, 2) ,9)
# print(x)
# x = np.empty((5, 2))
# print(x)
# x = np.eye(7)
# print(x)
# a = [[1, 2, 3], [4, 5, 6]]
# print(np.array(a))
# np.zeros_like(shape, 속성)
# np.ones_like(shape, 속성)
# np.full_like(shape, 속성)
# np.empty_like(shape, 속성)
# arr1 = np.zeros_like(a)
# print(arr1)
# arr1 = np.ones_like(a)
# print(arr1)
# arr1 = np.full_like(a, 5)
# print(arr1)
# arr1 = np.empty_like(a)
# print(arr1)
# -------------------------------------------------
# np.linspace(시작, 종료, 등분의 갯수, 속성)
# a1 = np.linspace(0, 1, 5)
# print(a1)
# a1 = np.linspace(0, 1)  # default = 50 개
# print(a1)
# a1 = np.linspace(0, 1, endpoint=False)  # 마지막값 포함 여부
# print(a1)
# a1 = np.linspace(0, 1, dtype=int)  # 타입지정
# print(a1)
# np.arange(시작, 종료, 스텝, [dtype])
# a1 = np.arange(0, 10, 2)  # 0부터 10까지 2씩 증가값 !! 마지막 종료값은 포함 안됨
# print(a1)  # [0 2 4 6 8]
# a1 = np.arange(10)
# print(a1)  # [0 1 2 3 4 5 6 7 8 9]
# -------------------------------------------------------
# 난수데이터 생성
# np.random.normal([속성]) -> 표준정규분포를 따름 평균 0 표준편차 1
# loc : 평균 , scale : 표준편차, size : shape
# a = np.random.normal(loc=0, scale=1, size=(2,3))
# print(a)
# np.random.randint(시작, 종료)
# a = np.random.randint(10, 20, size=(5,))
# print(a)  # [10 18 15 16 18]
# a1 = np.arange(10)
# print(a1)
# print(a1[3])
# print(a1[5:8])
# a2 = a1[5:8]
# print(a2)
# a2[0] = 10
# print(a2)  # 넘파이배열의 조각은 원본배열의 뷰
# print(a1)
#
# a1 = np.arange(10)
# a3 = a1[5:8].copy()
# a3[0] = 99
# print(a3)
# print(a1)
# a1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(a1)
# print(a1[:2])
# print(a1[:, :1])
# a1[:2, 1] = 0  # a1[:2, 1] = 0
# print(a1)
# -----------------------------------------------------
# 분리추출
# np.random.seed(9)  # random값을 고정
# colors = np.array(
#     ['red', 'orange', 'blue', 'red', 'blue', 'orange', 'orange'])
# print(colors)
# data = np.random.randn(7, 4)
# print(data)
# print(colors == 'orange')
# print(data[colors == 'orange'])
# print('--'*30)
# print(data[colors == 'blue', :2])
# --------------------------------------------
# x = np.arange(12)
# print(x)
# print(x.reshape((3, 4)))
# print(x.reshape((2, 3, 2)))
# print(x.reshape((3,5)))  # cannot reshape array of size 12 into shape (3,5)
# y = np.arange(20)
# print(y)
# y = y.reshape(4, -1)  # -1: reshape에서 한번만 사용할수 있다
# print(y)              # -1: -1을 제외한 나머지 값을 계산하여 대입한다.
# y = y.reshape(2, -1, 2)
# print(y)
# -------------------------------------------------------------
# (2, 3) X (2, 3) = err
# (2, 3) X (3, 2) = (2, 2)
# (2, 4) X (4, 3) = (2, 3)
# x = np.array([[1, 2, 3], [4, 5, 6]])  # (2,3)
# print(x)
# y = np.array([[1, 0, -1], [1, 1, 0]])  # (2,3)
# print(y)
# print(np.dot(x, y))  # err: shapes (2,3) and (2,3) not aligned: 3 (dim 1) != 2 (dim 0)
# print(y.T)  # (2,3) -> (3,2)
# print(np.dot(x, y.T))  # (2,3) X (3,2) = (2,2)
# print(x.T)
# print(np.dot(x.T, y))  # (3,2) X (2,3) = (3,3)

# 입출력
# data = np.loadtxt('data/heights.csv', skiprows=1, delimiter=',')
# data = np.loadtxt('data/heights.csv', skiprows=1, delimiter=',', unpack=True)  # 세로값 부터 읽기
# print(data)
# ------------------------------------------------------------

# a = np.random.randint(0,10, size=(2,4))
# print(a)
# np.savetxt('data/num.csv', a, delimiter=',')

# a = np.random.randint(0, 10, size=(2,4))
# print(a)
# np.save('data/arr1', a)
#
# b = np.random.randint(0, 10, size=(30))
# c = np.random.randint(0, 10, size=(2, 3, 4))
# print(b)
# print(c)
# np.savez('data/arr2', a, b, c)

# np.load()
print(np.load('data/arr1.npy'))
print(np.load('data/arr2.npz'))  # <numpy.lib.npyio.NpzFile object at 0x0000005D07D0DCF8>
print(np.load('data/arr2.npz').files)  # ['arr_0', 'arr_1', 'arr_2']
print(np.load('data/arr2.npz')['arr_0'])  # [[4 7 5 8] [3 6 9 5]]