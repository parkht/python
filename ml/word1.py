# 파이썬 패키지가 모여있는 사이트
# https://www.lfd.uci.edu/~gohlke/pythonlibs/
# 설치 : pip install wordc탭
# from wordcloud import WordCloud
# import matplotlib.pyplot as plt
# source = open('data\\alice.txt').read()
# # print(source)
# wc = WordCloud(background_color='yellow')
# w = wc.generate(source)
# plt.imshow(w)
# plt.axis('off')
# plt.show()
# --------------------------------------------------------------------
# from PIL import Image
# from wordcloud import WordCloud
# import matplotlib.pyplot as plt
# import numpy as np
# img = Image.open('img\\aliceImg3.png')
# mask = np.array(img)  # byte 배열 생성
# # print(mask)
# source = open('data\\alice.txt').read()
# wc = WordCloud(mask=mask, background_color='skyblue', width=600, height=600)
# w = wc.generate(source)
# plt.imshow(w)
# plt.axis('off')
# plt.show()
# ---------------------------------------------------------------------------
# from PIL import Image
# from wordcloud import WordCloud
# import matplotlib.pyplot as plt
# import numpy as np
# # 불필요한 단어제거
# from wordcloud import STOPWORDS
# sw = set(STOPWORDS)
# # print(sw)
# # STOPWORDS에 단어 등록
# sw.add('alice')
# sw.add('said')
# img=Image.open('img\\aliceImg3.png')
# mask=np.array(img)  #byte 배열생성
# # print(mask)
# source=open('data\\alice.txt').read()
# wc=WordCloud(mask=mask,background_color='yellow', stopwords=sw)
# w=wc.generate(source)
# plt.imshow(w)
# plt.axis('off')
# plt.show()
# ---------------------------------------------------------------------
from PIL import Image
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
# 불필요한 단어제거
from wordcloud import STOPWORDS
sw = set(STOPWORDS)
# print(sw)
# STOPWORDS에 단어 등록
sw.add('yesterday')
img=Image.open('img\\korea.jpg')
mask=np.array(img)  #byte 배열생성
# print(mask)
source=open('data\\yesterday.txt').read()
wc=WordCloud(mask=mask,background_color='blue', stopwords=sw)
w=wc.generate(source)
plt.imshow(w)
plt.axis('off')
plt.show()