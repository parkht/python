import pandas as pd
# data = pd.read_csv('data/gap.tsv', sep='\t')
# print(data)
# print(type(data))  # 데이터 프레임
# print(data.head())  # default = 5
# print(data.tail(7))  # 뒤에서 7개의 데이터만 보이게 하자
# print('--'*30)
# print(data.shape)  # 행과 열  # (1704, 6)
# print(data.shape[0])  # 행의 수  # 1704
# print(data.shape[1])  # 열의 수  # 6
# print(data.columns)  # 열의 이름
# print(data.dtypes)  # 각 열의 자료형
# pandas에서는 문자열을 string 대신에 object로 나타낸다.
# print(data['country'].head(3)) # country칼럼만 나타내고 위에서 3번째 까지만 나타내라
# print(data[['country', 'continent']].tail())
# 1개의 열 추출시 시리즈
# print(type(data['country']))  # <class 'pandas.core.series.Series'>
# 2개이상의 열 추출시 데이터 프레임
# print(type(data[['country', 'continent']].tail()))  # <class 'pandas.core.frame.DataFrame'>
# data1 = data[['country', 'continent', 'year']]  # 열단위 데이터 추출
# print(data1)
# 행단위 데이터 추출
# loc: 인덱스를 기준으로 행 데이터 추출
# iloc: 행번호를 기준으로 데이터 추출
# https://grouplens.org/datasets/movielens/
# baby = pd.read_csv('data/baby/yob1880.txt', names=['name', 'sex', 'births'],
#                    index_col='name')
# print(baby.head())
# print(baby.shape)
# print(baby.iloc[2])  # 표시는 되지 않지만
# print(baby.iloc[[1, 3, 5, 6, 7]])
# print(baby.iloc[-1])
# print(baby.loc['Mary'])
# print(baby.loc[['Mary', 'Margaret']])
# baby = pd.read_csv('data/baby/yob1880.txt', names=['name', 'sex', 'births'])
# print(baby.iloc[[1,3,5,7,9]])
# print(baby.loc[[1,3,5,7,9]])
# print('iloc: ', baby.iloc[-1])  # 행 번호 검색 iloc  # -1: 행의 마지막번 출력 가능
# print('loc: ', baby.loc[-1])  # 인덱스 검색 loc  # 인덱스 값에 -1이 없기 때문에 error
# data = pd.read_csv('data/gap.tsv', sep='\t')  # \t(탭)으로 데이터 구분
# print(data.head())
# print(data[['continent', 'year']])
# print(data.loc[[100,200]])
# print('--'*30)
# print(data.iloc[[100,200,-1]])
# print('--'*30)
# print(data.loc[[500, 1000, 1500],['country', 'year', 'lifeExp']])
# print('--'*30)
# print(data.iloc[[500, 1000, 1500],[0, 2, 3,-1]])  # iloc는 번호로 지정
# print(data.loc[:, ['year', 'lifeExp']])
# print(data[['year', 'lifeExp']])  # print(data.loc[:, ['year', 'lifeExp']])와 결과값이 같다
# print('--'*30)
# print(data.iloc[:,:4])
# print(data.head())
# 연도별 수명계산
# print(data.groupby('year')['lifeExp'].mean())  # 년도별 lifeExp의 평균
# ----------------------------------------------------------------
# 시리즈 생성 -> 열이 1개 인것  열 2개 이상부터는 dataframe
# s1 = pd.Series(['banana', 3000])
# print(s1)
# print('--'*30)
# s2 = pd.Series(['둘리', '희동이', '고길동'])
# print(s2)
# print('--' * 30)
# # ----------------------------------------------------------------
# # 데이터 프레임
# d1 = pd.DataFrame({
#     'name': ['둘리', '희동이', '고길동'],
#     'age': [7, 2, 40],
#     'birth': ['2013-01-01', '2019-12-30', '1980-01-30']
# })
# print(d1)
# ----------------------------------------------------------
# 시리즈의 메서드
# data = pd.read_csv('data/gap.tsv', sep='\t')
# s1 = data['year']
# print(s1)
# print(type(s1))
# print(s1.min())
# print(s1.mean())
# print(s1.sum())
# print(s1.max())
# 불리추출
# d1 = data[data['country'] == 'Afghanistan']
# print(d1)
# test = [False, False, False, False, False, True, False, False, False, True, False, False]
# print(d1[test])  # True인 데이터만 출력
# print(d1[d1['pop'] % 2 == 0])
# d1에서 gdpPercap의 평균보다 큰 행만 출력
# print('mean: ', d1['gdpPercap'].mean())
# print(d1[d1['gdpPercap'] > d1['gdpPercap'].mean()])
baby = pd.read_csv('data/baby/yob1880.txt', header=None,
                   names=['name', 'sex', 'births'])
# 남자 아기들만 위에서 20명 출력
# print(baby)
# print(baby[baby['sex']=='M'].head(20))
# 여자아기중 출생아수가 10명 미만인 것들만 출력 and:(조건1)&(조건2), or:(조건1)|(조건2)
# print(baby[(baby['sex']=='F') & (baby['births'] < 10)])
# 출생아수의 평균보다 작은 이름을 가진 남자아기 출력
print(baby['births'].mean())  # 100.743
print(baby[(baby['births'] < baby['births'].mean()) & (baby['sex']=='M')])






