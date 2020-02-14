import pandas as pd
import matplotlib.pyplot as plt

from matplotlib import font_manager, rc
fontname = font_manager.FontProperties(fname='malgun.ttf').get_name()
rc('font', family=fontname)

# baby = pd.read_csv("data/baby/yob1880.txt", names=["name", "sex", "births"])
# print(baby)
temp = []
for year in range(1880, 2011):
    filename = 'data/baby/yob{}.txt'.format(year)
    # print(filename)
    df = pd.read_csv(filename, names=["name", "sex", "births"])
    df['year'] = year
    temp.append(df)

data = pd.concat(temp, ignore_index=True)
# print(data)
# print(data[data['name']=='Mary'])
# 연도, 성별에 따른 출생자수
# total_births = data.pivot_table(index='year', columns='sex', values='births', aggfunc='sum')
# print(total_births)
#
# plt.plot(total_births)
# plt.title('연도별 신생아 성별 수')
# plt.legend(['여자', '남자'])
# plt.show()


def get_top1000(x):
    return x.sort_values(by='births', ascending=False)[:1000]


# print(data)
# top1000 = data.groupby(['year', 'sex']).apply(get_top1000)
# print(type(top1000))
# --------------------------------------------------------
# top1000['no'] = range(len(top1000))
# print(top1000)
# top1000 = top1000.set_index('no')  # index와 column에 중복되어져 있는 index를 'no' 칼럼으로 대채하면서 제거
# total_birth = top1000.pivot_table(index='year', columns='name', values='births', aggfunc=sum)
# print(total_birth)
# sample = total_birth[['Mary', 'Anna', 'Jane', 'Tom', 'John', 'William']]
# plt.plot(sample)
# plt.legend(['Mary', 'Anna', 'Jane', 'Tom', 'John', 'William'])
# plt.ylabel('출생아수')
# plt.yticks([10000, 30000, 50000, 70000, 90000])
# plt.show()

# ---------------------------------------------------------------------
# 년도별, 성별 이름이 전체 출생수에서 차지하는 비율
print(data[(data['year'] == 1880) & (data['sex'] == 'F')])
s1 = data[(data['year'] == 1880) & (data['sex'] == 'F')]
print(s1['births'].sum())  # 90993
s1['rate'] = s1.births/s1.births.sum()
print(s1)


def cal_rate(x):
    x['rate'] = x.births / x.births.sum()
    return x


print(data.groupby(['year', 'sex']).apply(cal_rate))