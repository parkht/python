# pip install JPype1-0.7.2-cp36-cp36m-win_amd64.whl
# pip install konlpy
from konlpy.tag import Hannanum, Kkma, Twitter
# h = Hannanum()
# malist = h.pos('침체된 경기를 활성화한다는 취지에선 긍정적이지만, 자칫 세금 낭비가 우려된다는 지적도 나온다.')
# print(malist)
# k = Kkma()
# malist = k.pos('침체된 경기를 활성화한다는 취지에선 긍정적이지만, 자칫 세금 낭비가 우려된다는 지적도 나온다.')
# print(malist)
# UserWarning: "Twitter" has changed to "Okt" since KoNLPy v0.4.5.
# t = Twitter()
# malist = t.pos('침체된 경기를 활성화한다는 취지에선 긍정적이지만, 자칫 세금 낭비가 우려된다는 지적도 나온다.')
# print(malist)
# -----------------------------------------------------------------------------
# from konlpy.tag import Okt
# o = Okt()
# malist = o.pos('침체된 경기를 활성화한다는 취지에선 긍정적이지만, 자칫 세금 낭비가 우려된다는 지적도 나온다.',
#                norm=True, stem=True)
# print(malist)
# ------------------------------------------------------------------------
# from konlpy.corpus import kolaw
# from konlpy.tag import Okt
# source = kolaw.open('constitution.txt').read()
# # print(source)
# o = Okt()
# # source에서 명사만 추출 nouns
# nouns = o.nouns(source)
# # print(nouns)
# # 단어 제외 시키기
# nouns = [n for n in nouns if (len(n)!=1) & (n != '로써') & (n != '그때')]
# # for n in nouns:
# #     if len(n) != 1:
#         # print(n, end=' ')
# # print(nouns)
# # print(len(nouns))
# import nltk
# from wordcloud import WordCloud
# import matplotlib.pyplot as plt
# from PIL import Image
# import numpy as np
# text = nltk.Text(nouns)
# # print(text)
# data = text.vocab()  # 단어의 빈도수
# # print(data)
# # 상위단어 추출 : most_common()
# data700 = data.most_common(700)
# # print(data700)
# dic = dict(data700)
# # print(dic)  # 딕셔너리 변환
# # 워드클라우드
# img = Image.open('img\\korea.jpg')
# mask = np.array(img)
# wc = WordCloud(font_path='malgun.ttf', mask=mask, background_color='yellow')
# # 자료형태가 딕셔너리 이기때문에 wc.generate_from_frequencies 사용
# w = wc.generate_from_frequencies(dic)
# plt.imshow(w)
# plt.axis('off')
# plt.show()
# 네이버 뉴스에서 '코로나'와 관련된 기사 300건을 검색하여
# title, description의 내용으로 워드 클라우드
# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import os
import sys
import json
import pandas as pd
import urllib.request
client_id = "hVv8LeNTyyMyn87KIYOL"
client_secret = "ih0TigXoyF"
encText = urllib.parse.quote("코로나")
url = "https://openapi.naver.com/v1/search/news.json?display=100&query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    data1 = response_body.decode('utf-8')
else:
    print("Error Code:" + rescode)

client_id = "hVv8LeNTyyMyn87KIYOL"
client_secret = "ih0TigXoyF"
encText = urllib.parse.quote("코로나")
url = "https://openapi.naver.com/v1/search/news.json?start=101&display=100&query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    data2 = response_body.decode('utf-8')
else:
    print("Error Code:" + rescode)

client_id = "hVv8LeNTyyMyn87KIYOL"
client_secret = "ih0TigXoyF"
encText = urllib.parse.quote("코로나")
url = "https://openapi.naver.com/v1/search/news.json?start=201&display=100&query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    data3 = response_body.decode('utf-8')
else:
    print("Error Code:" + rescode)

data1 = json.loads(data1)
# print(data1)
data2 = json.loads(data2)
# print(data2)
data3 = json.loads(data3)
# print(data3)
with open('data\\korona.csv', 'w', encoding='utf-8') as f:
    for dic in data1['items']:
        title = dic['title']
        description = dic['description']
        title = title.replace('<b>코로나</b>', '코로나')
        title = title.replace('&quot;', '')
        title = title.replace('...', '')
        title = title.replace('"', '')
        title = title.replace(',', ' ')
        title = title.replace("'", "")
        title = title.replace('[', '')
        title = title.replace(']', '')
        description = description.replace('<b>코로나</b>', '코로나')
        description = description.replace('&quot;', '')
        description = description.replace('...', '')
        description = description.replace('"', '')
        description = description.replace(',', ' ')
        description = description.replace("'", "")
        description = description.replace('[', '')
        description = description.replace(']', '')

        str = '{}, {}\n'.format(title, description)
        f.write(str)
with open('data\\korona.csv', 'a', encoding='utf-8') as f:
    for dic in data2['items']:
        title = dic['title']
        description = dic['description']
        title = title.replace('<b>코로나</b>', '코로나')
        title = title.replace('&quot;', '')
        title = title.replace('...', '')
        title = title.replace('"', '')
        title = title.replace(',', ' ')
        title = title.replace("'", "")
        title = title.replace('[', '')
        title = title.replace(']', '')
        description = description.replace('<b>코로나</b>', '코로나')
        description = description.replace('&quot;', '')
        description = description.replace('...', '')
        description = description.replace('"', '')
        description = description.replace(',', ' ')
        description = description.replace("'", "")
        description = description.replace('[', '')
        description = description.replace(']', '')

        str = '{}, {}\n'.format(title, description)
        f.write(str)
with open('data\\korona.csv', 'a', encoding='utf-8') as f:
    for dic in data3['items']:
        title = dic['title']
        description = dic['description']
        title = title.replace('<b>코로나</b>', '코로나')
        title = title.replace('&quot;', '')
        title = title.replace('...', '')
        title = title.replace('"', '')
        title = title.replace(',', ' ')
        title = title.replace("'", "")
        title = title.replace('[', '')
        title = title.replace(']', '')
        description = description.replace('<b>코로나</b>', '코로나')
        description = description.replace('&quot;', '')
        description = description.replace('...', '')
        description = description.replace('"', '')
        description = description.replace(',', ' ')
        description = description.replace("'", "")
        description = description.replace('[', '')
        description = description.replace(']', '')

        str = '{}, {}\n'.format(title, description)
        f.write(str)
from konlpy.corpus import kolaw
from konlpy.tag import Okt
source = open('data\\korona.csv', encoding='utf-8').read()
# print(source)
o = Okt()
# source에서 명사만 추출 nouns
nouns = o.nouns(source)
print(nouns)
# # 단어 제외 시키기
nouns = [n for n in nouns if (len(n)!=1) & (n != '코로나') & (n != '코로나19')]
print(nouns)
# # print(len(nouns))
import nltk
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
text = nltk.Text(nouns)
# # print(text)
data = text.vocab()  # 단어의 빈도수
# # print(data)
# # 상위단어 추출 : most_common()
data700 = data.most_common(700)
# # print(data700)
dic = dict(data700)
# # print(dic)  # 딕셔너리 변환
# # 워드클라우드
img = Image.open('img\\korea.jpg')
mask = np.array(img)
wc = WordCloud(font_path='malgun.ttf', mask=mask, background_color='yellow')
# # 자료형태가 딕셔너리 이기때문에 wc.generate_from_frequencies 사용
w = wc.generate_from_frequencies(dic)
plt.imshow(w)
plt.axis('off')
plt.show()









