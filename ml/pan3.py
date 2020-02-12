import pandas as pd
from numpy import NaN, nan, NAN
import seaborn as sns
# print(NaN == True)
# print(NaN == False)
# print(NaN == 0)
# print(NAN == '')
# print(pd.isnull(NAN))
# print(pd.isnull(nan))
# print(pd.notnull(NaN))
ebola = pd.read_csv('data/timeseries.csv')
# print(ebola)
# 누락값 처리(fillna(), interpolate(), dropna())
# d1 = ebola.iloc[:10, :5]
# print(d1)
# print(d1.fillna(0))
# print(d1.fillna(method='ffill'))  # 결측치를 앞의 데이터로 채우기
# print(d1.fillna(method='bfill'))  # 결측치를 뒤의 데이터로 채워라
# print(d1.interpolate())  # 결측치 압뒤의 데이터 평균으로 채워라
# 누락값의 처리(삭제)
# print(d1.dropna())
# d1['total'] = d1['Cases_Guinea'] + d1['Cases_Liberia'] + d1['Cases_SierraLeone']
# d1['total'] = d1['Cases_Guinea'].fillna(0) + d1['Cases_Liberia'].fillna(0) + d1['Cases_SierraLeone'].fillna(0)
# print(d1)
# print(d1['Cases_Liberia'].sum(skipna=False))
# print(d1.Cases_Liberia.sum())
# -------------------------------------------------
# 피벗
# data = {
#     "도시": ["서울", "서울", "서울", "부산", "부산", "부산", "인천", "인천" ],
#     "연도": ["2015", "2010", "2005", "2015", "2010", "2005", "2015", "2010" ],
#     "인구": [9904312, 9631482, 9762546, 3448737, 3393191, 3512547, 2890451, 2632035],
#     "지역": ["수도권", "수도권", "수도권", "경상권", "경상권", "경상권", "수도권", "수도권"]
# }
# df = pd.DataFrame(data)
# print(df)
# pivot(행인덱스, 열인덱스, 데이터)
# print(df.pivot('도시', '연도', '인구'))
# p1 = df.pivot('도시', '연도', '인구')
# print('p1.index : ', p1.index)
# print('p1.columns : ', p1.columns)
# p2 = p1.reset_index()
# print(p2)
# print('p2.index : ', p2.index)
# print('p2.columns : ', p2.columns)
# pivot_table(데이터, 행인덱스, 열인덱스)
# print(df.pivot_table('인구', '도시', '연도'))
# data = pd.read_excel('data/판매현황.xlsx')
# print(data)
# print(data.pivot_table(values='금액', index='분류', aggfunc='sum'))
# print(data.pivot(index='분류', values='금액'))  # pivot : 중복데이터가 있으면 사용 불가능
# print(data.pivot_table(index=['분류', '상품코드', '상품명'], values='금액', aggfunc='sum'))

# ----------------------------------------------------------
# melt(id_vars:위치를 유지할 열이름, var_name:열의 이름, value_name:값의 이름)
# pew = pd.read_csv('data/pew.csv')
# print(pew)
# print(pew.shape)
# d1 = pew.iloc[:6,:4]
# print(d1)
# print('--'*30)
# print(d1.melt(id_vars='religion', var_name='income', value_name='inwon'))

# print(ebola)
# print(ebola.columns)
# print(ebola.melt(id_vars=['Date', 'Day'], var_name='Country', value_name='Count'))
# ebola2 = ebola.melt(id_vars=['Date', 'Day'], var_name='Country', value_name='Count')
# print(ebola2.Country)
# print('--'*30)
# print(ebola2.Country[1947])
# print(ebola2.Country[0].split('_'))  # ['Cases', 'Guinea']
# print(ebola2.Country[0].split('_')[1])  # Guinea
# 문자열 처리시 str접근자 사용, 날짜형 처리시 dt접근자 사용
# 특정한 열에 한꺼번에 접근 하고 싶은 경우
# ebola3 = ebola2.Country.str.split('_')
# print(ebola3.str.get(0))
# print(ebola3.str.get(1))
# ebola2['status'] = ebola3.str.get(0)
# ebola2['country'] = ebola3.str.get(1)
# print(ebola2)
# ebola2['new'] = ebola2['status'] + ebola2['country']
# print(ebola2)
# -----------------------------------------------------
# print(ebola.info())
# print(ebola.head())
# ebola['Date'] = pd.to_datetime(ebola['Date'])
# print(ebola.info())
# print(ebola.Date[0].year)
# print(ebola.Date[0].month)
# print(ebola.Date[0].day)
# ebola['year'] = ebola['Date'].dt.year
# ebola['month'] = ebola['Date'].dt.month
# ebola['day'] = ebola['Date'].dt.day
# print(ebola)

# -------------------------------------------------------------
# 형변환(astype())
tips = sns.load_dataset('tips')
print(tips)
print(tips.info())
tips['sex'] = tips['sex'].astype(str)
print(tips.info())
tips['total_bill'] = tips['total_bill'].astype(str)
print(tips.info())
tips['total_bill'] = tips['total_bill'].astype(float)
print(tips.info())