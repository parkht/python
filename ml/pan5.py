import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# matplot의 한글처리
from matplotlib import font_manager, rc
fontname = font_manager.FontProperties(fname='malgun.ttf').get_name()
rc('font', family=fontname)

# tips = sns.load_dataset("tips")
# print(tips.head(10))
# tips10 = tips.sample(10, random_state=42)  # sample() -> 랜덤값 추출, random_state= -> 랜덤값의 고정
# print(tips10)
# g1 = tips10.groupby('sex')
# print(g1)  # 그룹객체
# # 그룹객체의 속성 groups
# print(g1.groups)
# avg = g1.mean()  # 그룹속성의 객체는 연산가능한 컬럼에 대해서만 계산됨
# print(avg)
# male = g1.get_group('Male')
# print(male)  # 그룹속성의 특정한 그룹을 가져옴
# print(type(male))  # <class 'pandas.core.frame.DataFrame'>

# g2 = tips10.groupby(['sex', 'time'])  # 그룹객체
# print(g2.mean())
# print(type(g2))  # <class 'pandas.core.groupby.generic.DataFrameGroupBy'>
# print(g2.index)  # AttributeError: 'DataFrameGroupBy' object has no attribute 'index'
# print(g2.columns)  # AttributeError: 'DataFrameGroupBy' object has no attribute 'columns'
# 그룹객체는 index나 column의 속성을 가지고 있지 않는다.
# df = g2.mean()  # type은 DataFrame, index는 multi-index
# print(df)
#  리셋인덱스
# df2 = df.reset_index()
# print(df2)
# df3 = df.set_index('tip')
# print(df3)

# -----------------------------------------------------
# gap = pd.read_csv('data/gap.tsv', sep='\t')
# 년도별로 수명의 평균을 출력
# df1 = gap.groupby('year')
# print(df1['lifeExp'].mean())
# 그룹객체와 agg메서드, apply메서드
def avg(x):
    print('*', x, '[', len(x), ']')
    hap = 0
    for i in x:
        hap = hap + i
    return hap / len(x)

# print(df1.lifeExp.apply(avg))
# globalavg = gap.lifeExp.mean()
# print(globalavg)

def avg2(x, globalavg):
    hap = 0
    for i in x:
        hap = hap + i
    return globalavg-hap/len(x)

# print(gap.groupby('year').lifeExp.agg(avg2, globalavg = globalavg))
# agg : 여러개 집계 메서드를 한번에 사용가능
# apply : 한개의 집계 메서드를 사용가능
# print(gap.groupby('year').agg({'lifeExp':'mean', 'pop':'median', 'gdpPercap':'max' }))


def f1(x):
    return 1


# iris = pd.read_csv('data/iris3.csv', sep=' ')
# print(iris.head())
# g= iris.groupby('Species')
# print('--'*30)
# print(g.apply(f1))
# print('--'*30)
# print(g.agg(f1))

# -----------------------------------------------
# lambda x:x*2 x를 입력받아서 x*2를 출력한다.
def ff1(x):
    return x*2


def hap(x):
    return x.sum()


# df = pd.DataFrame({"name":["Foo", "Baar", "Foo", "Baar"],
#                    "score_1":[5,10,15,10],
#                    "score_2" :[10,15,10,25],
#                    "score_3" : [10,20,30,40]})
# print(df)
# print(df.groupby(['name', 'score_1']).score_2.apply(hap))
# print(df.groupby(['name', 'score_1']).score_2.apply(lambda x:x.sum()))

# print(tips.head())

# tips['tip_rate'] = tips['tip'] / tips['total_bill']
# print(tips)

# sex_smoker = tips.groupby(['sex', 'smoker'])
# print('--'*30)
# print(sex_smoker.tip_rate.mean())
import numpy as np
# print(tips.groupby('day').apply(np.mean))
# print('--'*30)
# print(tips.groupby('day').transform(np.mean))

# tips10 = tips.head(10)
# tips10.loc[[1, 3, 7], 'total_bill'] = np.nan
# print(tips10)
# print(tips10['total_bill'].mean())  # 18.067
# print(tips10['total_bill'].fillna(0))
#
#
# def f3(x):
#     avg = x.mean()
#     return x.fillna(avg)
#
#
# print(tips10.groupby('sex').total_bill.transform(f3))  # 성별에 따른 평균 : 남여평균이 다름
# print(tips10.total_bill.transform(f3)) # 남여의 전체의 평균값
# -------------------------------------------------------------
# 누락된 날짜 추가 -> 데이터는 빈 값으로 채우기
ebola = pd.read_csv('data/timeseries.csv')
# print(ebola)
# print(list(range(0,5)))
# https://datascienceschool.net/view-notebook/8959673a97214e8fafdb159f254185e9/
# date_range 함수의 옵션
# print(pd.date_range(start='2020-02-14', end='2020-04-30', freq='w'))

# d1 = ebola.head()
# print(d1)
# d1['Date'] = pd.to_datetime(d1['Date'])  # Date 타입이 string -> 타입을 Date 변경
# d1 = d1.set_index('Date')
# print(d1)
# d1 = d1.reindex(pd.date_range(start='2014-12-31', end='2015-01-05'))
# d1['Day'] = range(284, 290)
# print(d1)
# ---------------------------------------------------------------------
d2 = ebola.tail(10)
print(d2)
print(d2.info())
d2['Date'] = pd.to_datetime(d2['Date'])
d2 = d2.set_index('Date')
print(d2)
d2 = d2.reindex(pd.date_range(start='2014-03-22', end='2014-04-04'))
print(d2)
d2 = d2.reset_index()
print(d2)
