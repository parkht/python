import random

import tensorflow as tf
# a = tf.constant([5, 100, 1, 2])
# b = tf.constant([[1, 2, 3], [4, 5, 6], [1, 1, 1]])
# with tf.Session() as sess:
#     print(sess.run(a))
#     print(sess.run(tf.argmax(a, 0)))
#     print(sess.run(tf.argmin(a, 0)))
#     print(sess.run(b))
#     print(sess.run(tf.argmax(b, 0)))
#     print(sess.run(tf.argmax(b, 1)))

# -----------------------------------------------------
from tensorflow.examples.tutorials.mnist import input_data
import matplotlib.pyplot as plt
mnist = input_data.read_data_sets("../mnist/data/", one_hot=True)
# print(mnist.train)
# print(mnist.train)
# print('학습데이터의 갯수', mnist.train.num_examples)
# print('검증데이터의 갯수', mnist.test.num_examples)
# print('학습데이터의 10001째 데이터', mnist.train.images[10000])
# plt.imshow(mnist.train.images[10000].reshape(28,28), cmap='Greys', interpolation='nearest')
# plt.show()
# print('학습데이터의 10001째 정답', mnist.train.labels[10000])
# print('학습데이터의 10001째 데이터 차원', mnist.train.images[10000].shape)
# plt.imshow(mnist.test.images[1000].reshape(28, 28), cmap='Greys', interpolation='nearest')
# plt.show()
# print('학습데이터의 1001째 정답', mnist.train.labels[1000])
# print('학습데이터의 1001째 데이터 차원', mnist.train.images[1000].shape)

# ------------------------------------------------------------------
#          y = xw + b = [None, 784][784, ???] + b =
# [None, 10] = xw + b = [None, 784][784, ???] + b
# [None, 10] =        = [None, ???]           + b
# [None, 10] =        = [None, 10]            + [10]
#                   w =            [784, 10]
# x = tf.placeholder(tf.float32, [None, 784])  # x = 학습용 데이터
# y = tf.placeholder(tf.float32, [None, 10])  # y = 데이터 정답
# w = tf.Variable(tf.random_normal([784, 10]))
# b = tf.Variable(tf.random_normal([10]))
# # 분류 -> 10가지(0~9)중 1가지를 선택하는 다중분류
# # 다중분류 : tf.nn.softmax()
# h = tf.nn.softmax(tf.matmul(x,w) + b)
# cost = tf.reduce_mean(-tf.reduce_sum(y * tf.log(h), axis=1))
# train = tf.train.GradientDescentOptimizer(0.2).minimize(cost)
# with tf.Session() as sess:
#     sess.run(tf.global_variables_initializer())  # 초기화
#     # r = sess.run(h, feed_dict={x:mnist.train.images[10000:10001]})
#     # print(r)
#     # print(sess.run(tf.argmax(r, 1)))
#     # ==학습==
#     for i in range(1001):
#         batch_x, batch_y = mnist.train.next_batch(1000)
#         t, c = sess.run([train, cost], feed_dict={x:batch_x ,y:batch_y})
#         # t, c = sess.run([train, cost], feed_dict={x:mnist.train.images, y:mnist.train.labels})
#         if i%100 == 0:
#             # print(c)
#             corr = tf.equal(tf.argmax(h, 1), tf.argmax(y,1))
#             # 두개의 값이 같으면 1, 다르면 0
#             acc = sess.run(tf.reduce_mean(tf.cast(corr, tf.float32)), feed_dict={x:mnist.train.images, y:mnist.train.labels})  # 평균 = 정확도가 나온다.
#             print(acc*100,'%')
#     # === 검증 ===
#     r = random.randint(0, mnist.test.num_examples-1)
#     print('실제 정답', sess.run(tf.argmax(mnist.test.labels[r:r+1], 1)))
#     plt.imshow(mnist.test.images[r:r+1].reshape(28,28), cmap='Greys', interpolation='nearest')
#     plt.show()

# --------------------------------------------------------------------
import numpy as np
data = np.loadtxt('data/zoo/zoo.csv', delimiter=',')
# print(data)
# print(data.shape)
xdata = data[:, 0:16]
ydata = data[:, [-1]]
# print(xdata.shape)  # (101, 15)
# print(ydata.shape)  # (101, 1)
x = tf.placeholder(tf.float32, [None, 16])
y = tf.placeholder(tf.int32, [None, 1])  # 형태의 변한을 해야함 0~6 -> 1000000~0000001
# y = tf.placeholder(tf.float32, [None, 7])
w = tf.Variable(tf.random_normal([16, 7]))
b = tf.Variable(tf.random_normal([7]))
# y = xw + b -> [None, 7] = [None, 16] * [16, 7] + b
#            -> [None, 7] = [None, 7]            + [7]
sess = tf.Session()
sess.run(tf.global_variables_initializer())
onehot = tf.one_hot(y,7)  # 0~6 -> 1000000~0000001 형태의 변환 실행
# print(sess.run(onehot, feed_dict={y:ydata}))  # 결과값이 3차원으로 나옴 2차원으로 바꿔주야한다.
onehot = tf.reshape(onehot, [-1, 7])  # 3차원: [[[]], [[]]...[[]]] -> 2차원: [[],[]...[]] 3차원을 2차원으로 변환
# print(sess.run(onehot, feed_dict={y:ydata}))
logits = tf.matmul(x, w) + b
h = tf.nn.softmax(logits)
tempcost = tf.nn.sigmoid_cross_entropy_with_logits(logits=logits, labels=onehot)
cost = tf.reduce_mean(tempcost)
train = tf.train.GradientDescentOptimizer(0.7).minimize(cost)
for i in range(2001):
    sess.run(train, feed_dict={x:xdata, y:ydata})
    if i%100 == 0:
        print(i, sess.run(cost, feed_dict={x:xdata, y:ydata}))
corr = tf.equal(tf.argmax(h, 1), tf.argmax(onehot, 1))
acc = tf.reduce_mean(tf.cast(corr, tf.float32))
print(sess.run(acc, feed_dict={x:xdata, y:ydata}))
sample = [[1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 4, 1, 1, 0]]
print('예측 : ', sess.run(tf.argmax(h, 1), {x:sample}))