import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.examples.tutorials.mnist import input_data
# a = tf.constant(10, name='a1')
# b = tf.constant(5, name='b')
# print(a)
# print(b)
# op = a + b
# # op = tf.add(a, b)
# v = tf.Variable(0)  # v는 변수이고 초기값을 0으로 정의 하라(실행을 해야 초기화 및 값을 가짐)
# op2 = tf.assign(v, op)  # op의 결과를 v에 넣으라는 것을 op2에 정의 하라
# sess = tf.Session()
# sess.run(tf.global_variables_initializer())  # 변수 초기화 실행
# print(sess.run(v))  # 0
# print(sess.run([a, b, op, v]))  # a, b, op를 실행  [10, 5, 15, 0]
# print(sess.run([op2, v]))  # op2를 실행, v의 값 [15, 15]
# sess.close()
# -----------------------------------------------------------------------
# a = tf.placeholder(tf.int32)  # a = tf.placeholder(np.int32)
# b = tf.placeholder(np.int32)  # tf.placeholder는 초기화 하지 않음
# c = tf.placeholder(tf.int32)  # tf.placeholder는 실행시 값을 넣어줌
# op1 = a + b
# op2 = op1 * c  # tf.multiply(op, c)
# with tf.Session() as sess:
#     print(sess.run(a, feed_dict={a: 3}))
#     print(sess.run(op1, feed_dict={a: 3, b: 4}))
#     print(sess.run([op2, op1], feed_dict={a: [1, 2], b: [3, 4], c: 5}))

# ----------------------------------------------------------------------
# state = tf.Variable(0)
# one = tf.constant(1)
# new_value = tf.add(state, one)  # state + one
# update = tf.assign(state, new_value)  # state = new_value(state + one)
# init = tf.global_variables_initializer()  # 변수 초기화
# sess = tf.Session()
# sess.run(init)
# for x in range(5):
#     print('--'*30)
#     print('start_state : ',sess.run(state))
#     print('update : ', sess.run(update))
#     print('end_state : ', sess.run(state))
# sess.close()

# -----------------------------------------------------------------
# a = tf.constant([1, 2, 3, 4, 5, 6, 7, 8, 9])
# b = tf.constant([[[1, 1],[2, 2]],[[3, 3],[4, 4]]])
# op1 = tf.reshape(a, [3,3])
# with tf.Session() as sess:
#     result = sess.run(op1)
#     print(result)
#     print(sess.run(b))
#     print(sess.run(tf.reshape(b, [4, -1])))

# -----------------------------------------------------------------
# pip install opencv-python
import cv2
# img = cv2.imread('img/winter2.jpg')
# 이미지 보여주기
# plt.imshow(cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
# plt.axis('off')
# plt.show()

# 이미지 저장하기
# cv2.imwrite('img/wn2.jpg', img)

# 이미지 리사이징
# img2 = cv2.resize(img, (200,200))
# cv2.imwrite('img/wn3.jpg', img2)
# plt.imshow(cv2.cvtColor(img2, cv2.COLOR_RGB2BGR))
# plt.show()
# print(img2)  # [[[76 58 27][76 58 27][76 58 27]...[31 27 51][25 22 48][23 21 50]]]
# print(type(img2))  # <class 'numpy.ndarray'>
# print(img2.shape)  # (200, 200, 3)
# img3 = img2[150:300, 20:100]
# plt.imshow(cv2.cvtColor(img3,cv2.COLOR_RGB2BGR))
# plt.show()

# ----------------------------------------------------------------------
# mnist = input_data.read_data_sets('../mnist/data/', one_hot=True)
# one_hot
# 0 : 1000000000
# 1 : 0100000000
# 2 : 0010000000
# 7 : 0000000100
# 9 : 0000000001
# print(mnist.train)  # train 학습용 데이터, 정답
# print(mnist.test)  # test 검증용 데이터, 정답
# 데이터의 갯수
# print('학습데이터 갯수 : ', mnist.train.num_examples)  # 55,000
# print('검증데이터 갯수 : ', mnist.test.num_examples)  # 10,000
# 실제데이터 이미지
# print(mnist.train.images[10])
# plt.imshow(mnist.train.images[10].reshape(28,28), cmap='Greys',
#            interpolation='nearest')
# plt.show()
# print('정답 : ', mnist.train.labels[10])

# ----------------------------------------------------------
# dan = tf.placeholder(tf.int32)
# one = tf.constant(1)
# v = tf.Variable(0)
# op1 = tf.assign(v, v + one)
# op2 = dan * v
# with tf.Session() as sess:
#     sess.run(tf.global_variables_initializer())  # 변수 초기화
#     for i in range(9):
#         sess.run(op1)
#         r, d, t = sess.run([dan, v, op2], feed_dict={dan: 5})
#         print(r,' * ', d,' = ', t)

# ------------------------------------------------------------------
# num = tf.placeholder(tf.int32)
# one = tf.constant(1)
# v = tf.Variable(0)
# op1 = tf.assign(v, v + one)
# hap = tf.Variable(0)
# op2 = tf.assign(hap, hap + v)
# with tf.Session() as sess:
#     sess.run(tf.global_variables_initializer())  # 변수 초기화
#     for i in range(sess.run(num, feed_dict={num: 15})):
#         print(sess.run([op1, op2]))

# ---------------------------------------------------------------------
num = tf.placeholder(tf.int32)
one = tf.constant(1)
v = tf.Variable(0)
hap = tf.Variable(0)
op = tf.assign(v, v + one)
op2 = tf.assign(hap, 1 + (v-1)*num)
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(10):
        sess.run(op)
        result = sess.run(op2, feed_dict={num:2})
        if  result > 10:
            break
        else: print(result)




