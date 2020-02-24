import cv2
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
def mosaic(img, area, size):
    (x1, y1, x2, y2) = area
    temp = img[y1:y2, x1:x2]
    small = cv2.resize(temp, (size,size))  # 축소
    temp = cv2.resize(small, (x2-x1, y2-y1), interpolation=cv2.INTER_AREA)  #크기원상복귀(모자이크처리)
    tempimg = img.copy()
    tempimg[y1:y2,x1:x2] = temp
    return tempimg


# img1 = cv2.imread('img/winter2.jpg')
# print(img1)
# plt.imshow(cv2.cvtColor(img1, cv2.COLOR_RGB2BGR))
# plt.axis('off')
# plt.show()
# 모자이크 처리
# img2 = mosaic(img1,(50,120,180,280),10)
# plt.imshow(cv2.cvtColor(img2, cv2.COLOR_RGB2BGR))
# plt.axis('off')
# plt.show()

# ------------------------------------------------
# 얼굴인식
# https://github.com/opencv/opencv/tree/master/data/haarcascades
# img = cv2.imread('img/naun.jpg')
# plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
# plt.show()
# cascade_file = 'face.xml'
# cascade = cv2.CascadeClassifier(cascade_file)
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# face = cascade.detectMultiScale(img_gray, minSize=(50, 50))
# if len(face) == 0:
#     print('실패')
#     quit()
#
# print(face)
# for (x, y, w, h) in face:
#     img = mosaic(img, (x, y, x+w, y+h), 10)
#
# plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
# plt.show()

#---------------------------------------------------------------
# 여러명의 얼굴인식
# https://github.com/opencv/opencv/tree/master/data/haarcascades
# img = cv2.imread('img/april.jpg')
# plt.imshow(cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
# plt.show()
# cascade_file = 'face.xml'
# cascade = cv2.CascadeClassifier(cascade_file)
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# face = cascade.detectMultiScale(img_gray, minSize=(50, 50))
# if len(face) == 0:
#     print('실패')
#     quit()
#
# print(face)
# for (x, y, w, h) in face:
#     img = mosaic(img, (x, y, x+w, y+h), 10)
#
# plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
# plt.show()

# ---------------------------------------------------------------
# import tensorflow as tf
# xtrain = [1, 2, 3]  # 학습 데이터
# ytrain = [1, 2, 3]  # 정답
# # y = wx + b
# w = tf.Variable(0.1)
# b = tf.Variable(0.1)
#
# h = w * xtrain + b  # 모델
# cost = tf.reduce_mean(tf.square(h - ytrain))  # tf.평균(tf.제곱(h - ytrain)
# train = tf.train.GradientDescentOptimizer(0.01).minimize(cost)
# with tf.Session() as sess:
#     sess.run(tf.global_variables_initializer())
#     # 학습
#     for i in range(5001):
#         sess.run(train)
#         if i%100 == 0:
#             print(i, sess.run(cost), sess.run(w), sess.run(b))

# ------------------------------------------------------------------------
# x = tf.placeholder(tf.float32, shape=[None])
# y = tf.placeholder(tf.float32, shape=[None])
# w = tf.Variable(tf.random_normal([1]))
# b = tf.Variable(tf.random_normal([1]))
# h = w * x + b
# cost = tf.reduce_mean(tf.square(h - y))
# train = tf.train.GradientDescentOptimizer(0.01).minimize(cost)
# with tf.Session() as sess:
#     sess.run(tf.global_variables_initializer())
#     for i in range(3001):
#         t, c, ww, bb = sess.run([train, cost, w, b], feed_dict={x:[1,2,3,4,5], y:[2,4,3,6,4]})
#         if i%100 == 0:
#             print(i, c, ww, bb)
#
#     # 예측
#     print(sess.run(h, feed_dict={x:[10, 20, 30]}))

# ---------------------------------------------------------------------
# data = np.loadtxt('data/cars.csv', skiprows=1, delimiter=',', unpack=True)
#                                  1줄건너띄기,  ','로 구분  , 세로로 먼저 읽어라
# print(data)  # [[][]]
# print(data[0])  # 데이터
# print(data[1])  # 정답
# x = tf.placeholder(tf.float32, [None])
# y = tf.placeholder(tf.float32, [None])
# w = tf.Variable(0.2)
# b = tf.Variable(0.2)
# h = w * x + b
# cost = tf.reduce_mean(tf.square(h - y))
# train = tf.train.GradientDescentOptimizer(learning_rate=0.0037).minimize(cost)
# with tf.Session() as sess:
#     sess.run(tf.global_variables_initializer())
#     for i in range(3001):
#         sess.run(train, feed_dict={x:data[0], y:data[1]})
#         if i%100 == 0:
#             print(i, sess.run(cost, feed_dict={x:data[0], y:data[1]}), sess.run(w))
#
#     # 예측
    # print(sess.run(h, feed_dict={x:[0, 30]}))
    # result = sess.run(h, feed_dict={x:[0, 30]})
    # plt.plot([0,30], result)
    # plt.plot(data[0], data[1], 'o')
    # plt.show()

# ----------------------------------------------------------------
x = [1, 2, 3]
y = [1, 2, 3]
w = tf.placeholder((tf.float32))
h = w * x
cost = tf.reduce_mean(tf.square(h - y))
with tf.Session() as sess:
    clist = []
    wlist = []
    for i in range(-30, 50):
        temp_w = i * 0.1  # -3 ~ 5를 0.1단위로 변경
        cc, ww = sess.run([cost, w], feed_dict={w:temp_w})
        clist.append(cc)
        wlist.append(ww)
    plt.plot(wlist, clist)
    plt.show()






