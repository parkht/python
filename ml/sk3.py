# import glob

# print(ord('a'))  # 97
# print(ord('A'))  # 65
# print(chr(65))  # A
# print(chr(97))  # a
# a = [1, 2, 3, 4, 5, 6]
# total = sum(a)
# print(total)  # a의 내용을 더해라 -> 21
# # map(함수, 반복가능객체)
# # lambda 입력:출력
# print(map(lambda x:2*x, a))  # <map object at 0x000000A0C66152E8>
# # list를 써야지만 내용을 볼수 있다.
# print(list(map(lambda x:2*x, a)))  # [2, 4, 6, 8, 10, 12]
# print(list(map(lambda x:x/total, a)))
# print(glob.glob('data\\*.*'))  # ['data\\20-02-07.csv', 'data\\20-02-10.csv',....]
# print(os.path.basename('d:\\git_hub\\python\\ml')  # ml
# print(os.path.basename('d:\\git_hub\\python\\ml\\movie.py')  # movie.py

# -------------------------------------------------------------------------
# import glob, os
# from sklearn.svm import SVC
# from sklearn.metrics import accuracy_score, classification_report
#
#
# def makedata(f):
#     with open(f, encoding='utf-8') as f:
#         text = f.read()
#         text = text.lower()
#         code_a = ord('a')
#         code_z = ord('z')
#         cnt = [0 for n in range(26)]  # a~z 까지 count를 위해 0으로 초기화
#         for c in text:
#             if code_a <= ord(c) <= code_z:
#                 cnt[ord(c)-code_a] = cnt[ord(c)-code_a] + 1
#         total = sum(cnt)
#         rate = list(map(lambda x:x/total, cnt))
#         # print(rate)
#         return rate
#
#
# def load_files(path):
#     files = glob.glob(path)  # 리스트
#     # print(files)
#     x = []  # 데이터
#     y = []  # 정답
#     for f in files:
#         rate = makedata(f)
#         x.append(rate)
#         # print(f, '--', os.path.basename(f)[:2])
#         y.append(os.path.basename(f)[:2])
#     return {'data':x, 'label':y}
#     # print(y)
#
#
# train = load_files('data\\lang\\train\\*.*')
# # load_files함수를 사용해서 나온 x, y를 trainx, trainy에 대입
# # print(train)
# test = load_files('data\\lang\\test\\*.*')
# print(test)
#
# model = SVC()  # 모델생성
# model.fit(train['data'], train['label'])  # 훈련
# pred = model.predict(test['data'])  # 예측
# acc = accuracy_score(pred, test['label'])
# cl_report = classification_report(test['label'], pred)
# print('정확도 : ', acc)
# print('리포트 = \n', cl_report)

# -----------------------------------------------------------------
# import urllib.request as req
# local= "mushroom.csv"
# url = "https://archive.ics.uci.edu/ml/machine-learning-databases/mushroom/agaricus-lepiota.data"
# req.urlretrieve(url, local)
# print("ok")
# import pandas as pd
# dates=[['2019-01-01','2019-01-02','2019-01-03','2019-01-04'],
#        ['2019-02-01', '2019-02-02', '2019-02-03', '2019-02-04']]
# df = pd.DataFrame(dates, columns=['a', 'b', 'c', 'd'])
# print(df)
# for d in df:
#     print(d)
# for k, v in df.iteritems():
#     print('k: ',k)  # 열 이름
#     print('v: ', v)  # 열 데이터
# for k,v in df.iterrows():
#     print(k)  # 행 인덱스
#     print(v)  # 행 데이터
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
df = pd.read_csv('data/mushroom.csv', header=None)
# print(df.head())
label = []
data = []
for index,value in df.iterrows():
    label.append(value[0])  # 정답
    temp = []
    for d in value[1:]:
        # print(d)
        temp.append(ord(d))
    data.append(temp)  # 데이터
trainx, testx, trainy, testy = train_test_split(data, label, test_size=0.25)
model = RandomForestClassifier()
model.fit(trainx, trainy)
pred = model.predict(testx)
score = accuracy_score(pred, testy)
print('정확도 : ', score)







