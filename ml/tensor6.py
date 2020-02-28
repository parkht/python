import tensorflow as tf
import numpy as np
import pandas as pd
data=np.loadtxt('data/iris3.csv', dtype=np.float32, skiprows=1)
print(data.shape)
# 70%의 데이터로 학습, 30%데이터로 정확도를 검증
# 여러분류중 하나를 선택하는 다중분류이기 때문에 tf.nn.softmax()를 사용한다.
# 0~2 (원핫기법 적용전) => 100, 010, 001 (원핫기법 적용)
np.random.shuffle(data)
trainx, trainy = data[:105, :4], data[:105, 4:]
testx, testy = data[105:, :4], data[105:, 4:]
# print(trainx)
# print(trainy)
x = tf.placeholder(tf.float32, [None, 4])
y = tf.placeholder(tf.float32, [None, 3])
w = tf.Variable(tf.random_normal([4, 3]))
b = tf.Variable(tf.random_normal([3]))
z = tf.matmul(x, w) + b
h = tf.nn.softmax(z)

tempcost = tf.nn.sigmoid_cross_entropy_with_logits(logits=z, labels=y)
cost = tf.reduce_mean(tempcost)
train = tf.train.GradientDescentOptimizer(0.55).minimize(cost)
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(1001):
        sess.run(train, feed_dict={x:trainx, y:trainy})
        if i%100 == 0:
            print(sess.run(cost, feed_dict={x:trainx, y:trainy}))
    pred = sess.run(h, feed_dict={x:testx})
    # print(pred)
    corr = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
    acc = tf.reduce_mean(tf.cast(corr, tf.float32))
    print('정확도 = ', sess.run(acc, feed_dict={x:testx, y:testy}))

# ----------------------------------------------------------------------
# data = np.loadtxt('data/zoo/zoo.csv', delimiter=',')
# trainx = data[:, :16]
# trainy = data[:, [-1]]  # 0~6 ==> 원핫기법 적용전
# print(trainx)
# print(trainy)
# x = tf.placeholder(tf.float32, [None, 16])
# y = tf.placeholder(tf.int32, [None, 1])  # tf.nn.one_hot()을 사용하기 위해서는 int로 사용해야된다.
# w = tf.Variable(tf.random_normal([16, 7]))
# b = tf.Variable(tf.random_normal([7]))
#
# onehot1 = tf.one_hot(y, 7)  # tf.one_hot() : 0->1000000, 1:0100000, 2: 0010000.... 6: 0000001로 바꾸라는 함수
# with tf.Session() as sess:
#     sess.run(tf.global_variables_initializer())
#     print(sess.run(onehot1, feed_dict={y:trainy}))
#     onehot2 = tf.reshape(onehot1, [-1, 7])
#     z = tf.matmul(x, w) + b
#     # 여러분류중 하나를 선택하는 다중분류이기 때문에 tf.nn.softmax()를 사용한다.
#     h = tf.nn.softmax(z)
#     tempcost = tf.nn.sigmoid_cross_entropy_with_logits(logits=z, labels=onehot2)
#     cost = tf.reduce_mean(tempcost)
#     train = tf.train.GradientDescentOptimizer(2.0).minimize(cost)
#     # === 학습 ===
#     for i in range(2001):
#         sess.run(train, feed_dict={x:trainx, y:trainy})
#         if i%100 == 0:
#             print(i, sess.run(cost, feed_dict={x:trainx, y:trainy}))
#
#     # === 정확도(검증) ===
#     corr = tf.equal(tf.argmax(h, 1), tf.argmax(onehot2, 1))
#     acc = tf.reduce_mean(tf.cast(corr, tf.float32))
#     print(sess.run(acc, feed_dict={x:trainx, y:trainy}))
#     sample = [[1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 4, 1, 1, 0]]
#     print('예측 : ',sess.run(tf.argmax(h, 1), feed_dict={x:sample}))

# --------------------------------------------------------------------
# bmi2.csv를 읽어 15000건은 학습용, 5000 건은 검증용
# data = np.loadtxt('data/bmi2.csv', delimiter=',', skiprows=1)
# # print(data)
# trainx = data[:15000, :2]
# trainy = data[:15000, 2:]
# # print(trainx)
# # print(trainy)
# testx = data[15000:, :2]
# testy = data[15000:, 2:]
# # print(testx)
# # print(testy)
# x = tf.placeholder(tf.float32, [None, 2])
# y = tf.placeholder(tf.float32, [None, 3])
# w = tf.Variable(tf.random_normal([2, 3]))
# b = tf.Variable(tf.random_normal([3]))
# h = tf.nn.softmax(tf.matmul(x, w) + b)
# cost = -tf.reduce_sum(y * tf.log(h))
# train = tf.train.GradientDescentOptimizer(0.0011).minimize(cost)
# with tf.Session() as sess:
#     sess.run(tf.global_variables_initializer())
#     for i in range(3001):
#         sess.run(train, feed_dict={x:trainx, y:trainy})
#         if i%100 == 0:
#             print(i, sess.run(cost, feed_dict={x:trainx, y:trainy}))
#     # 정확도
#     corr = tf.equal(tf.argmax(h, 1), tf.argmax(y, 1))
#     acc = tf.reduce_mean(tf.cast(corr, tf.float32))
#     print(sess.run(acc, feed_dict={x:testx, y:testy}))

# -------------------------------------------------------------------------
# cars.csv를 읽어 속도가 50일때의 제동거리를 예측하세요(회귀)
# data = np.loadtxt('data/cars.csv', delimiter=',', skiprows=1, unpack=True)
# print(data)
# # data[0] => 데이터, data[1] => 정답
# x = tf.placeholder(tf.float32, [None])
# y = tf.placeholder(tf.float32, [None])
# w = tf.Variable(tf.random_normal([1]))
# b = tf.Variable(tf.random_normal([1]))
# h = w*x + b
# cost = tf.reduce_mean(tf.square(h - y))
# train = tf.train.GradientDescentOptimizer(0.0035).minimize(cost)
# with tf.Session() as sess:
#     sess.run(tf.global_variables_initializer())
#     for i in range(3001):
#         sess.run(train, feed_dict={x:data[0], y:data[1]})
#         if i%100 == 0:
#             print(sess.run(cost, feed_dict={x:data[0], y:data[1]}))
#     print('예측 : ', sess.run(h, feed_dict={x:[50]}))




