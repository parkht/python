from bs4 import BeautifulSoup
import urllib.request as req

# html 가져오기
url = 'http://finance.naver.com/marketindex/'
res = req.urlopen(url)

# html 분석하기
soup = BeautifulSoup(res, 'html.parser')

# 원하는 데이터 추출하기
price = soup.select_one('div.head_info > span.value').string
print('usd/krw = ',price)