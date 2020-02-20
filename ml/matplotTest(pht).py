import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# matplot의 한글처리
from matplotlib import font_manager, rc
fontname = font_manager.FontProperties(fname='malgun.ttf').get_name()
rc('font', family=fontname)

# 1번--------------------------------------------------------------
report = pd.read_csv('data/report.csv')
report_df = pd.DataFrame(report)
# print(report_df.columns)
# print(report_df.head(10))
# print(report_df.tail(10))
# print('--'*30)

# 2번---------------------------------------------------------------
# report_df_nh = report_df[report_df['State']=='New Hampshire']
# print(report_df_nh)
# plt.scatter(report_df_nh['Beer'], report_df_nh['Wine'])
# plt.xlabel('Beer')
# plt.ylabel('Wine')
# plt.show()

# 3번---------------------------------------------------------------
# report_df_beer = report_df.pivot_table(index='Year', columns='State', values='Beer')
# print(report_df_beer)
# report_df_beer = report_df_beer[['New Hampshire', 'Colorado', 'Utah']]
# print(report_df_beer)
# plt.plot(report_df_beer)
# plt.title('주별 맥주 소비량의 변화')
# plt.legend(['New Hampshire', 'Colorado', 'Utah'])
# plt.xlabel('Year')
# plt.ylabel('Beer')
# plt.show()

# 4번-------------------------------------------------------------------
# tips = sns.load_dataset('tips')
# tips_lunch = tips[tips['time']=='Lunch'].total_bill
# print(tips_lunch.min())
# print(tips_lunch.max())
# print(tips_lunch.mean())
# print(tips_lunch.median())
# tips_dinner = tips[tips['time']=='Dinner'].total_bill
# plt.boxplot([tips_lunch, tips_dinner])
# plt.show()

# 5번-----------------------------------------------------------------

# tips = tips.pivot_table(index='size', columns='day', values='total_bill')
# print(tips)

# 6번----------------------------------------------------------------------
# plt.plot(tips)
# plt.title('식사 비용 현황')
# plt.legend(['Thur', 'Fri', 'Sat', 'Sun'])
# plt.xlabel('좌석수')
# plt.ylabel('식사비용')
# plt.show()

# 7번--------------------------------------------------------------------
# bank = pd.read_csv('data/bank.csv', parse_dates=['Closing Date', 'Updated Date'])
# print(bank.info())
#
# # 8번----------------------------------------------------------------------
# bank['year'] = bank['Closing Date'].dt.year
# closingyear = bank.groupby('year').size()
# print(closingyear)
# plt.bar(closingyear.index, closingyear.values)
# plt.title('연도별 파산한 은행수')
# plt.xticks(range(2000,2018))
# plt.show()