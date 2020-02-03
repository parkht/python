import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


sns.set(style="darkgrid")

# 데이터 가져오기
fmri = sns.load_dataset("fmri")
print(fmri.dtypes)
# fmri.astype({'timepoint' :'int32'}).dtypes

fmri.index = fmri.index.astype(np.int32)
fmri.timepoint = fmri.timepoint.astype(np.int32)
fmri.signal = fmri.signal.astype(np.float32)
# fmri.subject = fmri.subject.astype(np.string_)
# fmri.event = fmri.event.astype(np.string_)
# fmri.region = fmri.region.astype(np.string_)
# fmri = np.int32(fmri)

print(fmri.dtypes)
# 데이터 세팅
sns.relplot(x="timepoint", y="signal", kind="line", data=fmri)

plt.show()