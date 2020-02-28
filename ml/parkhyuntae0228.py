# import numpy as np
# import tensorflow as tf
# data = np.loadtxt('data\\product.csv', delimiter=',', skiprows=1, encoding='utf-8')
# # print(data[:, :2])
# trainx = data[:, :2]
# trainy = data[:, 2:]
# print(trainx)
# print(trainy)
# x = tf.placeholder(tf.float32, [None, 2])
# y = tf.placeholder(tf.float32, [None, 1])
#
# w = tf.Variable(tf.random_normal([2, 1]))
# b = tf.Variable(tf.random_normal([1]))
#
# h = tf.matmul(x, w) +b
# cost = tf.reduce_mean(tf.square(h - y))
# train = tf.train.GradientDescentOptimizer(0.03).minimize(cost)
# # 0.03 =  0.27537283
# # 0.012 = 0.2753729
# # 0.011 = 0.27538443
# # 0.01  = 0.27540264
# # 0.009 = 0.27540213
# with tf.Session() as sess:
#     sess.run(tf.global_variables_initializer())
#     for i in range(3001):
#         sess.run(train, feed_dict={x:trainx, y:trainy})
#         if i%200 == 0:
#             print(i, sess.run(cost, feed_dict={x:trainx, y:trainy}))
#     ww, bb = sess.run([w, b], feed_dict={x:trainx, y:trainy})
#     print('기울기 : ',ww)
#     print('절편 : ', bb)


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
data = pd.read_csv('data\\iris.csv')
# print(data)
# 'Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width', 'Species'
x = data.loc[:, ['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width']]
y = data.loc[:, ['Species']]
# print(x)
# print(y)
trainx, testx, trainy, testy = train_test_split(x, y, test_size=0.3, shuffle=True)
model = SVC()  # 모델
model.fit(trainx, trainy)  # 학습
pred = model.predict(testx)  # 예측
print('정확도 ; ', accuracy_score(pred, testy))


