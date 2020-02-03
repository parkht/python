import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="darkgrid")
# seaborn의 제공 데이터 가져오기
tips = sns.load_dataset("tips")
print(tips, type(tips))
# 전체 주문 금액과 팁의 관계
# sns.relplot(x="total_bill", y="tip", size="size", sizes=(15,200), data=tips)
# 전체 주문 금액과 팁의 관계 + 흡연자와 팁의 관계
# sns.relplot(x="total_bill", y="tip", hue="smoker", style="smoker", sizes=(15,200), data=tips)
# 전체 주문 금액과 팁의 관계 + 흡연자와 팁의 관계 + 시간과 팁의 관계
# sns.relplot(x="total_bill", y="tip", hue="smoker", style="time", sizes=(15,200), data=tips)

sns.relplot(x="total_bill", y="tip", hue="size", size="size", palette="ch:r=-.9, l=.75", sizes=(15,200), data=tips)


df = pd.DataFrame(dict(time=np.arange(500),
                       value=np.random.randn(500).cumsum()))
print(df, type(df))
g = sns.relplot(x="time", y="value", kind="line", data=df)

plt.show()