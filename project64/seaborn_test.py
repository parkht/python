import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


sns.set(style="darkgrid")

# 데이터 가져오기
fmri = sns.load_dataset("fmri")
# fmri.astype({'timepoint' :'int32'}).dtypes

# 데이터 세팅
sns.lineplot(x="timepoint", y="signal", hue='region', style='event', data=fmri)

plt.show()