from bs4 import BeautifulSoup
import urllib.request as req

# html 가져오기
url = 'http://finance.naver.com/marketindex/'
res = req.urlopen(url)

# html 분석하기
# 네이버 환율 자료가 'utf-8'이 아니기 때문에 from_encoding='euc-kr'로 엔코딩함
# 자료를 우선 출력하여 잘 나오는지 보고 정확하지 않을시 encoding확인
soup = BeautifulSoup(res, 'html.parser',from_encoding='euc-kr')
#print(soup)
# 원하는 데이터 추출하기
country_value = soup.select('a.head')
#print(country_value)
for i in country_value:
    #print(i)
    print(i.h3.string)
    k = i.select_one('div > span.value').string

    w = i.select_one('div > span > span.blind')
    #  중간에 w 값이 None이 있어서 if로 w값이 None이면 출력을 안하게 만들었음
    if w != None:
        print(k,w.string)
    else:
        print(k)