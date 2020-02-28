# import numpy as np
# import tensorflow as tf
# data = np.loadtxt('data\\product.csv', delimiter=',', skiprows=1, encoding='utf-8')
# # print(data[:, :2])
# trainx = data[:, :2]
# trainy = data[:, 2:]
# x = tf.placeholder(tf.float32, [None, 2])
# y = tf.placeholder(tf.int32, [None, 1])
# w = tf.Variable(tf.random_normal([2, 5]))
# b = tf.Variable(tf.random_normal([5]))
#
# onehot1 = tf.one_hot(y, 5)
# with tf.Session() as sess:
#     sess.run(tf.global_variables_initializer())
#     print(sess.run(onehot1, feed_dict={y:trainy}))
#     onehot2 = tf.reshape(onehot1, [-1, 5])
#     z = tf.matmul(x, w) + b
#     # 여러분류중 하나를 선택하는 다중분류이기 때문에 tf.nn.softmax()를 사용한다.
#     h = tf.nn.softmax(z)
#     tempcost = tf.nn.sigmoid_cross_entropy_with_logits(logits=z, labels=onehot2)
#     cost = tf.reduce_mean(tempcost)
#     train = tf.train.GradientDescentOptimizer(2.0).minimize(cost)
#     # 0.30377364 = 2.0
#     # 0.37552792 = 0.03
#     # === 학습 ===
#     for i in range(5001):
#         sess.run(train, feed_dict={x:trainx, y:trainy})
#         if i%500 == 0:
#             print(i, sess.run(cost, feed_dict={x:trainx, y:trainy}))
#     ww, bb = sess.run([w,b] , feed_dict={x:trainx, y:trainy})
#     print('기울기 : ', ww)
#     print('절편 : ', bb)
#     print('--'*30)
#     print(sess.run(h, feed_dict={x:[[3,3]]}))

# ------------------------------------------------------------
# scikit learn 선형회귀 방법
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score
import pandas as pd
data=pd.read_csv('data\\product.csv')
print(data.head())
print(data.shape)   #(264,3)
xdata=[]   # [[3,4],[3,3]....]
ydata=[]
a=list(data['제품_친밀도'])
# print(a)
b=list(data['제품_적절성'])
c=list(data['제품_만족도'])
for i in range(data.shape[0]):
    xdata.append([a[i],b[i]])
    ydata.append(c[i])
# print(xdata)
# print(ydata)
model=LinearRegression()
model.fit(xdata,ydata)
print('기울기',model.coef_)
print('절편',model.intercept_)
print(model.predict([[3,5]]))

