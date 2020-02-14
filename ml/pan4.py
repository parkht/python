import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# matplot의 한글처리
from matplotlib import font_manager, rc
fontname = font_manager.FontProperties(fname='malgun.ttf').get_name()
rc('font', family=fontname)

# tips = sns.load_dataset('tips')
# print(tips)
# tips2 = tips.head(10)
# print(tips2)
# -------------------------------------------------
# print(tips2.loc[[1,3,5,7,9],'total_bill'])
# tips2.loc[[1,3,5,7,9],'total_bill'] = 'notvalue'
# print(tips2)
# tips['total_bill'] = tips2['total_bill'].astype(float)  # could not convert string to float: 'notvalue'

# 잘못입력된 문자열처리(to_numeric)
# tips2['total_bill'] = pd.to_numeric(tips2['total_bill'])  # ValueError: Unable to parse string "notvalue" at position 1
# tips2['total_bill'] = pd.to_numeric(tips2['total_bill'], errors='coerce')
# print(tips2)
# print(tips2.info())

# tips2['total_bill'] = pd.to_numeric(tips2['total_bill'], errors='coerce', downcast='float')
# print(tips2)
# print(tips2.info())

# print(tips.info())
# tips['sex'] = tips['sex'].astype(str)
# print(tips.info())

# -------------------------------------------------------
# 함수


# def double(x):
#     return x*2
#
#
# def nth(x, n):
#     return x * n
#
#
# def selfprint(x):
#     print('**')
#     print(type(x))
#     print(x)
#
#
# def avg(x):
#     h = 0
#     print('x의 shape', x.shape[0])
#     for i in x:
#         h = h + i
#     return h/x.shape[0]
#
#
# df = pd.DataFrame({'a':[10, 20, 30, 40, 50],
#                   'b':[100, 200, 300, 400, 500]})
# print(df)
# print(df.a.sum())
# apply() -> 내가 정의한 함수를 Dataframe에 적용
# print(df.a.apply(double))  # print(df['a'].apply(double))
# print(df.a.apply(nth, n=5))
# 데이터 프레임에 적용
# print(df.apply(double))
# df.apply(selfprint)
# df.apply(selfprint, axis = 1)
# print(df.apply(avg))
# print(df.apply(avg, axis=1))

# ------------------------------------------------------------

#
def cnt_null(x):
    # print(x.shape)
    return x.shape[0] - x.count()


def rate_null(x):
    cnt = cnt_null(x)
    rate = cnt / x.shape[0]

    return rate


titanic = sns.load_dataset('titanic')
# print(titanic.info())
# print(titanic.apply(cnt_null))  # 누락값의 갯수를 구해라 def cnt_null(x):
titanic_null = titanic.apply(rate_null)

print(titanic_null)

# -------------------------------------------------------------


