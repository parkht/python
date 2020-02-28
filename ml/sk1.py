# https://scikit-learn.org/stable/tutorial/machine_learning_map/
# scikit-learn 어떤 알고리즘을 사용할지 선택하는 맵

# from sklearn.svm import LinearSVC
# from sklearn.metrics import accuracy_score
# data = [[0,0],[0,1],[1,0],[1,1]]
# label = [0,0,0,1]
# # 모델 생성
# model = LinearSVC()
# # 훈련
# model.fit(data, label)
# # 예측
# test_data = [[0,0],[0,1],[1,0],[1,1]]
# test_label = [0,0,0,1]
# pred = model.predict(test_data)
# # 평가(정확도)
# print('정확도 : ', accuracy_score(pred, test_label))

# from sklearn.svm import LinearSVC
# from sklearn.metrics import accuracy_score
# from sklearn.neighbors import KNeighborsClassifier
# data = [[0,0],
#         [0,1],
#         [1,0],
#         [1,1]]
# label = [0,1,1,0]
# model = KNeighborsClassifier(n_neighbors=1)
# model.fit(data, label)
# test_data = [[0,0],[0,1],[1,0],[1,1]]
# test_label = [0,1,1,0]
# pred = model.predict(test_data)
# print('정확도 : ', accuracy_score(test_label, pred))

# ---------------------------------------------------------------------
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.svm import SVC
# from sklearn.metrics import accuracy_score
# data = pd.read_csv('data/iris.csv')  # dataframe
# print(data)
# x = data.loc[:, ['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width']]
# y = data.loc[:, 'Species']
# # print(x.head())
# # print(y.head())
# trainx, testx, trainy, testy = train_test_split(x, y, test_size=0.2, shuffle=True)
# model = SVC()
# model.fit(trainx, trainy)
# pred = model.predict(testx)  # 예측
# print('정확도 : ', accuracy_score(pred, testy))

# -------------------------------------------------------------
# from sklearn import svm, metrics
# from sklearn.model_selection import train_test_split
# import matplotlib.pyplot as plt
# import pandas as pd
#
# # 키와 몸무게 데이터 읽어 들이기
# tb1 = pd.read_csv('data/bmi.csv')
#
# # 컬럼(열)을 자르고 정규화 하기
# label = tb1['label']
# w = tb1['weight']/100
# h = tb1['height']/200
# wh = pd.concat([w, h], axis=1)
#
# # 학습 전용 데이터와 테스트 전용 데이터로 나누기
# data_train, data_test, label_train, label_test = train_test_split(wh, label)
#
# # 데이터 학습
# clf = svm.SVC()
# clf.fit(data_train, label_train)
#
# # 데이터 예측
# predict = clf.predict(data_test)
#
# # 결과 테스트 하기
# ac_score = metrics.accuracy_score(label_test, predict)
# cl_report = metrics.classification_report(label_test, predict)
#
# print('정답률 : ', ac_score)
# print('리포트 : ', cl_report)
#
# tb1 = pd.read_csv('data/bmi.csv', index_col=2)
#
# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)
#
# def scatter(lbl, color):
#         b = tb1.loc[lbl]
#         ax.scatter(b['weight'], b['height'], c=color, label=lbl)
#
#
# scatter('fat', 'red')
# scatter('normal', 'yellow')
# scatter('thin', 'purple')
#
# ax.legend()
# plt.show()

# -----------------------------------------------------------




