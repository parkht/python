import tensorflow as tf
import numpy as np
# 상수노드 -> 프로그램이 돌아가는 중에는 값이 절대 변하지 않는다.
# c1 = tf.constant(3)
# print(c1)
# c2 = tf.constant(3, np.float32)
# print(c2)
# c3 = tf.constant([3, 4, 5])
# print(c3)
# 텐서플로의 실행
# sess = tf.Session()
# print(sess.run(c1))  # 3
# print(sess.run(c2))  # 3.0
# print(sess.run(c3))  # [3 4 5]
# sess.close()
# c1 = tf.constant(3)
# c2 = tf.constant(4)
# op1 = c1 + c2  # op1 = tf.add(c1, c2)
# op2 = tf.multiply(c1, c2)  # op2 = c1 * c2
# print(op1)  # Tensor("add:0", shape=(), dtype=int32)
# print(op2)  # Tensor("Mul:0", shape=(), dtype=int32)
# sess = tf.Session()
# print(sess.run(op1))  # 7
# print(sess.run(op2))  # 12
# print(sess.run([c1, c2, op1]))  # [3, 4, 7]
# ---------------------------------------------------------
# a = tf.constant(3, dtype=tf.int32, name='a1')
# b = tf.constant(4)
# c = tf.constant(5)
# d = tf.multiply(a, b)
# e = tf.add(c, d)
# f = tf.subtract(d, e)
# print(a)  # Tensor("a1:0", shape=(), dtype=int32)
# print(b)  # Tensor("Const:0", shape=(), dtype=int32)
# print(c)  # Tensor("Const_1:0", shape=(), dtype=int32)
# print(d)  # Tensor("Mul:0", shape=(), dtype=int32)
# print(e)  # Tensor("Add:0", shape=(), dtype=int32)
# print(f)  # Tensor("Sub:0", shape=(), dtype=int32)
#
# with tf.Session() as sess:
#     print(sess.run(e))
#     print(sess.run(f))
# -------------------------------------------------------
# 변수 1 : 변수는 반드시 초기화 후에 사용해야함!!
# a = tf.constant(3, dtype=tf.int32, name='a1')
# b = tf.constant(4)
# c = tf.constant(5)
# op = (a + b) * c
# v = tf.Variable(0)  # v를 변수 부분으로 정의
# op2 = tf.assign(v, op)  # op의 결과값을 v에 넣어라 (v <- op = (a + b) * c)
# with tf.Session() as sess:
#     sess.run(tf.global_variables_initializer())  # 변수 초기화
#     print(sess.run([v, op2]))
# -------------------------------------------------------------
# 행렬곱
# a = tf.constant([[1, 2, 3],[4, 5, 6]])
# print(a)
# print(a.get_shape())
# b = tf.constant([[1],[0],[1]])
# print(b.get_shape())
# op1 = tf.matmul(a, b)
# with tf.Session() as sess:
#     print(sess.run(op1))
# ---------------------------------------------------------
# 초기화
# a = tf.zeros_like([4, 3, 2])  # [0, 0, 0]
# b = tf.zeros([2, 2, 3])  # [[[0. 0. 0.]  [0. 0. 0.]] [[0. 0. 0.]  [0. 0. 0.]]]
# print(a)
# with tf.Session() as sess:
#     print(sess.run(a))
#     print(sess.run(b))

# ------------------------------------------------------------
# tf.placeholder()
# a = tf.placeholder(tf.int32, [None])
# b = tf.constant(2)
# op = a * b
# with tf.Session() as sess:
#     print(sess.run(op, feed_dict={a: [7, 5, 3]}))
#     print(sess.run(op, feed_dict={a: [8, 6, 4]}))
#     print(sess.run(op, feed_dict={a: [10, 20, 11, 12, 15, 27]}))
# --------------------------------------------------------------
x = np.random.randn(3, 4)
y = np.random.randn(4, 2)
print(x)
print("--"*30)
print(y)
print('--'*30)
a = tf.placeholder(tf.float32, shape=[3, 4])
b = tf.placeholder(tf.float32, shape=[4, 2])
op = tf.matmul(a, b)
with tf.Session() as sess:
    print(sess.run(op, feed_dict={a: x, b: y}))



