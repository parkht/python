from bs4 import BeautifulSoup
import urllib.request as req

url = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp'

# urlopen()으로 데이터 가져오기
res = req.urlopen(url)

# BeatifulSoup으로 분석하기
soup = BeautifulSoup(res, 'html.parser')

# 원하는 데이터 추출하기
title = soup.find('title').string
wf = soup.find('wf').string

print('title = ',title)
print('wf = ',wf)

print('모든 title 출력 -> ')
for i in soup.find_all('title'):
    print(i)

city = soup.find_all('city')

tmef = soup.find_all('tmef')

wf = soup.find_all('wf')

tmn = soup.find_all('tmn')

tmx = soup.find_all('tmx')
# wf : 날씨 tmn : 최저기온 txm: 최고기온

#print(soup)

a=0
b=13

for i in city:
    print('-----',i.string,'-----')
    for k in range(a,b):
        print('시간 :', tmef[k].string)
        print('날씨 :', wf[k+1].string)
        print('최저기온 :', tmn[k].string)
        print('최고기온 :', tmx[k].string)
    a= a+13
    b= b+13