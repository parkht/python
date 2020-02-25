# water.csv 파일은 총 정수기 대여 대수(전월), 10년이상 노후 정수기 대여 대수(전월),
# AS시간(당월)에 대한 데이터이다. 주변의 신규 아파트가 동시 입주함에 따라 가입자수가
# 늘어 다음달의 AS시간을 예측하고 이에 따라 신규인력을 채용하고자 한다.

# 1) 10년미만 정수기 대여수와 10년이상 노후 정수기 대여수에 따라 AS시간을 예측하는
# 모델을 # tensorflow를 활용하여 작성하고 최종 cost와 기울기, 절편을 출력하시오.
# 모델을 작성
import numpy as np
import tensorflow as tf
data = np.loadtxt('data/water.csv', delimiter=',', skiprows=1)
# print(data)  # data[0] = old, data[1] = new, data[2] = as_time
# print(trainy)
trainx = data[:, :2]
trainy = data[:, 2:]
print(trainx)
print(trainy)
x = tf.placeholder(tf.float32, [None, 2])
y = tf.placeholder(tf.float32, [None, 1])
w = tf.Variable(tf.random_normal([2, 1]))
b = tf.Variable(tf.random_normal([1]))
h = tf.nn.softmax(tf.matmul(x, w) + b)
cost = -tf.reduce_sum(y * tf.log(h))
train = tf.train.GradientDescentOptimizer(0.0001).minimize(cost)
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(3001):
        sess.run(train, feed_dict={x:trainx, y:trainy})
        if i%100 == 0:
            print(i, sess.run(cost, feed_dict={x:trainx, y:trainy}))


# 2) 월말 최종 대여수를 보니 총 대여수가 300,000대, 그중 10년 이상 노후 정수기
# 대수가 70,000대로 집계되었다. 다음달의 AS시간을 예측하고 그에 따라 필요한
# AS기사의 인원수를 예측하시오.
# 단)AS기사 1명이 한달간 처리하는 AS시간=8시간*20일