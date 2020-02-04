import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style='white', palette='muted', color_codes=True)
rs = np.random.RandomState(10)
print(rs, type(rs))

f, axes = plt.subplots(2, 2, figsize=(7, 7), sharex=True)
sns.despine(left=True)
print('f : ', f)
print('axes : ', axes)
d = rs.normal(size=100)
print('d : ', d)

# 막대 그래프 (kde=False : 선그래프 표시 X)
sns.distplot(d, kde=False, color='b', ax=axes[0, 0])

# 분포에 대한 표식(hist=False : 막대 그래프 표시 X)
sns.distplot(d, hist=False, rug=True, color='r', ax=axes[0, 1])

# 그래프의 안쪽 면의 채우기(kde_kws={'shade':True})
sns.distplot(d, hist=False, color='g', kde_kws={'shade': True}, ax=axes[1, 0])

# 막대 그래프와 선 그래프 표시
sns.distplot(d, color='m', ax=axes[1, 1])

plt.setp(axes, yticks=[])
plt.tight_layout()

plt.show()