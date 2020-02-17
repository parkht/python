import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# matplot의 한글처리
from matplotlib import font_manager, rc
fontname = font_manager.FontProperties(fname='malgun.ttf').get_name()
rc('font', family=fontname)

# d1 = json.load(open('data/foods.json', 'r', encoding='utf-8'))
# print(type(d1))  # 리스트 [{}, {}]
# print(len(d1))
# print(d1[0])
# print(d1[0]['nutrients'])
# nutrients = pd.DataFrame(d1[0]['nutrients'])
# print(nutrients)
# ----------------------------------------------------
# col = ['id', 'description', 'manufacturer', 'group']
# data = pd.DataFrame(d1, columns=col)
# print(data)
# temp = []
# for i in d1:
#     n = pd.DataFrame(i['nutrients'])
#     n['id'] = i['id']
#     temp.append(n)

# nutrients = pd.concat(temp, ignore_index=True)
# print(nutrients)
# print(nutrients.shape)
# nutrients = nutrients.drop_duplicates()
# print(nutrients.shape)
# --------------------------------------------------------
# 컬럼명 전체 변경
# ['id', 'description', 'manufacturer', 'group'] => ['id', 'food', 'manufacturer', 'fgroup']
# data.columns = ['id', 'food', 'manufacturer', 'fgroup']
# print(data.columns)
# 컬럼명 부분 변경
# data = data.rename(columns={'description':'food', 'group':'fgroup'})
# print(data)
# print(data.columns)
# print(nutrients.columns)
# df = data.merge(nutrients, on='id')
# print(df)
# print(df.info())




#------------------------------------------------------
# 중복데이터 처리
# data = {'key1':['a', 'b', 'b', 'c', 'c'],
#     'key2':['v', 'w', 'w', 'x', 'y'],
#     'col':[1, 2, 3, 4, 5]}
#
# df = pd.DataFrame(data)
# print(df)
# print(df.duplicated('key1'))
# print(df.duplicated(['key1', 'key2']))
# print(df.drop_duplicates(['key1'], keep='first'))  # key1에서 중복되는 것 중에 첫번째(first)를 살려라
# print(df.drop_duplicates(['key1'], keep='last'))  # key1에서 중복되는 것 중에 마지막(last)을 살려라
# print(df.drop_duplicates())   # 데이터 중에 모든값이 일치하는 값을 지워라

# -------------------------------------------------------------------
# 네이버 개발자센터에서 책을 검색하여 '파이썬'이란 단어로 책을 검새갛여 나온 json 문서를 데이터 프레임으로 변환

# from datetime import datetime
# t1 = datetime.now()
# t2 = datetime(1982,9,4)
# print(t1)
# print(t2)
# print(t1-t2)
#
# ebola = pd.read_csv('data/timeseries.csv')
# print(ebola.info())
# ebola['Date'] = pd.to_datetime(ebola['Date'])
# print(ebola.info())

# ebola = pd.read_csv('data/timeseries.csv', parse_dates=['Date'])
# print(ebola.info())
# ebola['yy'] = ebola['Date'].dt.year
# ebola['mm'] = ebola['Date'].dt.month
# ebola['dd'] = ebola['Date'].dt.day
# print(ebola)
# ebola 최초 발생일
# print(ebola['Date'].min())
# print(ebola['Date'].max())
# ebola['new'] = ebola['Date'] - ebola['Date'].min()
# print(ebola)
# ----------------------------------------------------------
bank = pd.read_csv('data/bank.csv', parse_dates=['Closing Date', 'Updated Date'])
# print(bank)
# 연도별 파산한 은행수 그래프
bank['year'] = bank['Closing Date'].dt.year
bank['quarter'] = bank['Closing Date'].dt.quarter
# print(bank.info())
# closingyear = bank.groupby('year').size()
# print(closingyear)
# plt.bar(closingyear.index, closingyear.values)
# plt.title('연도별 파산한 은행수')
# plt.xticks(range(2000,2018))
# plt.show()
# 연도별 분기별 파산한 은행수 그래프
closingyq = bank.groupby(['year', 'quarter']).size()
closingyq = closingyq.reset_index()
print(closingyq.info())
closingyq['yq'] = closingyq['year'].astype(str) + '-' + closingyq['quarter'].astype(str)
print(closingyq)
closingyq = closingyq.set_index('yq')
print(closingyq)
plt.plot(closingyq.index, closingyq[0])
plt.show()