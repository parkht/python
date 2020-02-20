import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# matplot의 한글처리
from matplotlib import font_manager, rc
fontname = font_manager.FontProperties(fname='malgun.ttf').get_name()
rc('font', family=fontname)
# data = pd.read_csv('data/gap.tsv', sep='\t')
# print(data.head())
# print(data.shape)
# print(data[data['country']=='Afghanistan'])
# d1 = data[data['country']=='Afghanistan']
# 브로드캐스팅 : 데이터 프레임 또는 시리즈의 모든 데이터에 대해 한꺼번에 연산
# print(d1['lifeExp']+d1['lifeExp'])
# print(d1['lifeExp'] + 100)
# s1 = pd.Series([100,200,300])
# print(s1)
# print(d1['lifeExp'] + s1) # 길이가 다른 벡터연산 -> 인덱스 값이 같을때 까지만 연산 나머지는 누락!!
# print(d1.sort_values(by='gdpPercap'))
# print(d1.sort_values(by='pop', ascending=False))  # by='pop' (값에 따라) ascending=False (역순정렬)
# print(d1.set_index('year'))  # year컬럼을 index 값으로 변경
# d1 = d1.set_index('year')
# print(d1.shape)  # year 칼럼을 index로 만들어서 칼럼숫자가 6에서 5로 변경
# print(d1.sort_index(ascending=False))  # index 기준으로 역순정렬
# ------------------------------------------------------------
# set_index(), reset_index(), reindex()
# d1 = d1.set_index('pop')
# print(d1)  # set_index() -> 기존 index를 삭제 후 지정된 컬럼을 index 지정
# d1 = d1.reset_index()
# print(d1)  # reset_index() -> 기존 index가 열이되고 일련번호가 index 지정
# d1 = d1.reindex([0, 1, 11, 2, 3, 4, 5, 6, 7, 8 ,9, 10])
# print(d1)  # index 순서변경 사용자 정의
# -------------------------------------------------------------
# 열의 추가 및 삭제
# d1['total'] = d1['lifeExp'] + d1['gdpPercap']
# print(d1)
# d1 = d1.drop('total', axis=1)  # axis = 1 열 방향 삭제
# print(d1)
# d1 = d1.drop(['lifeExp', 'gdpPercap'], axis=1)
# print(d1)
# d1.to_csv('data/d1.csv',index=False, header=False, sep=';')
# d1.to_clipboard()
# d1.to_json('data/di.json')
# d1.to_excel('data/d1.xlsx', index=False, header=False)
# d1.to_pickle('data/d1.pickle')
# d2 = pd.read_pickle('data/d1.pickle')  # 압축 형태 -> pickle
# print(d2)
# ---------------------------------------------------------
# 시각화 부분
# data = sns.load_dataset('anscombe')
# print(data)
# d1에 dataset이 I인것만 추출
# d1 = data[data['dataset']=='I']
# print(d1)
# d2 = data[data['dataset']=='II']
# print(d2)
# d3 = data[data['dataset']=='III']
# print(d3)
# d4 = data[data['dataset']=='IV']
# print(d4)
#
# fig = plt.figure()
# area1 = fig.add_subplot(2,2,1)
# area2 = fig.add_subplot(2,2,2)
# area3 = fig.add_subplot(2,2,3)
# area4 = fig.add_subplot(2,2,4)
#
# area1.plot(d1['x'],d1['y'], 'ro')
# area2.plot(d2['x'],d2['y'], 'o-')
# area3.plot(d3['x'],d3['y'], 'o--')
# area4.plot(d4['x'],d4['y'])
#
# area1.set_title('영역1')
# area2.set_title('영역2')
# area3.set_title('영역3')
# area4.set_title('영역4')
#
# fig.tight_layout()
# plt.show()

# ----------------------------------------------------------
# tips = sns.load_dataset('tips')
# print(tips)
# 산점도그래프
# 1.
# fig = plt.figure()
# area1 = fig.add_subplot(1, 1, 1)
# area1.scatter(tips['total_bill'], tips['tip'])  # 산점도 scatter(x축, y축)
# area1.set_title('식비와 팁과의 산점도')  # title 작성
# area1.set_xlabel('식비')
# area1.set_ylabel('팁')
# plt.show()
# 2.
# plt.scatter(tips['total_bill'], tips['tip'])
# plt.title('식비와 팁과의 산점도')
# plt.xlabel('식비')
# plt.ylabel('팁')
# plt.show()
# ---------------------------------------------------
# plt.scatter(tips['total_bill'], tips['tip'], s=tips['size']*15)
# plt.title('식비와 팁과의 산점도')
# plt.xlabel('식비')
# plt.ylabel('팁')
# plt.show()
# ----------------------------------------------------
# def sex_to_int(sex):
#     if sex == 'Female':
#         return 0
#     else :
#         return 1
# tips['sex2'] = tips['sex'].apply(sex_to_int)
# print(tips)
# plt.scatter(tips['total_bill'], tips['tip'],
#             s=tips['size']*15, c=tips['sex2'], alpha=0.5)
# plt.title('식비와 팁과의 산점도')
# plt.xlabel('식비')
# plt.ylabel('팁')
# plt.show()
# ---------------------------------------------------
# plt.hist(tips['total_bill'])
# plt.show()
# ---------------------------------------------------
# plt.boxplot(tips['total_bill'])
# plt.show()
# 여자가 계산한 식대를 그래프로
# print(tips[tips['sex'] == 'Female'])
# print(tips[tips['sex'] == 'Female']['total_bill'])
# print(tips[tips['sex'] == 'Female'].total_bill)
# plt.boxplot(tips[tips['sex'] == 'Female'].total_bill)
# plt.show()
# 여자, 남자가 계산한 식대를 그래프로
# plt.boxplot([tips[tips['sex'] == 'Female'].total_bill,
#              tips[tips['sex'] == 'Male'].total_bill], labels=['여','남'])
# plt.title('성별에 따른 식대')
# plt.xlabel('성별')
# plt.show()
# 1. 요일별 교통사고 사상자 합계(사상자 3명 이상인 데이터에 대해)
# data = pd.read_csv('data/accidentdata.csv')
# print(data)
# d1 = data[data['사상자수'] > 2]
# print(d1.shape)
# s1 = d1.groupby('요일')['사상자수'].sum()
# s1 = s1.reindex(['월', '화', '수', '목', '금', '토', '일'])
# plt.plot(s1)
# plt.title('2012-2014 요일별 교통사고 사망자수')
# plt.show()
# d2 = data[data['발생지시도'] == '경기']
# print(d2.shape)
# s2 = d2.groupby('발생지시군구')['사망자수'].sum()
# print(s2)
# s2 = s2.sort_values(ascending=False)
# print(s2.head())
# s2 = s2.head()
# plt.pie(s2, labels=['화성시', '평택시', '용인시', '수원시', '고양시'],
#         colors=['red','orange','green','yellow','blue'], autopct='%.2f%%')
# plt.title('2012-2014 경기도 교통사고 사망자수 top5')
# plt.show()
# -----------------------------------------------------
# d1 = pd.read_csv('data/concat_1.csv')
# d2 = pd.read_csv('data/concat_2.csv')
# d3 = pd.read_csv('data/concat_3.csv')
# print(d1)
# print(d2)
# print(d3)
# data = pd.concat([d1, d2, d3])
# print(data)
# print(data.loc[1])
# print(data.iloc[1])
# data = pd.concat([d1, d2, d3], ignore_index=True)  # 가지고 있는 index 무시 새로운 index지정
# print(data)
# data = pd.concat([d1, d2, d3], axis=1)  # axis=1 : 자료를 열방향으로 붙여라
# print(data)
# ---------------------------------------------
person = pd.read_csv('data/survey_person.csv')
site = pd.read_csv('data/survey_site.csv')
survey = pd.read_csv('data/survey_survey.csv')
visited = pd.read_csv('data/survey_visited.csv')
# print(person)
# print(site)
# print(survey)
# print(visited)

ps = person.merge(survey, left_on='ident', right_on='person')
# print(ps)
print(site)
print(visited)
sv = site.merge(visited, left_on='name', right_on='site')
print(sv)