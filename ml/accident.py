import pandas as pd
import matplotlib.pyplot as plt

from matplotlib import font_manager, rc
fontname = font_manager.FontProperties(fname='malgun.ttf').get_name()
rc('font', family=fontname)

data = pd.read_csv('data/accidentdata.csv')
print(data)
print(data.info())

# 요일별 / 발생지 시도별 교통사고 분석
date_death = data.pivot_table(index='요일', columns='발생지시도', values='사망자수', aggfunc='sum')
print(date_death)
date_death = date_death.reindex(['월', '화', '수', '목', '금', '토', '일'])

plt.plot(date_death)
plt.title('요일별/발생지시도별 사망자수')
plt.legend(date_death.columns)
plt.show()