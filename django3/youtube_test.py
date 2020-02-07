import os

import requests  # 특정웹사이트 접속
from bs4 import BeautifulSoup
url = 'https://www.youtube.com/channel/UCaJdckl6MBdDPDf75Ec_bJA'
recvd = requests.get(url)
# print(recvd)  # <Response [200]> 접속성공
# print(recvd.text)  # html코드 확인
dom = BeautifulSoup(recvd.text, 'lxml')  # lxml 파싱(잘못된 html 코드 수정)
# 이미지저장, (제목, 별점 등록일) --> webtoon.csv 저장
table = dom.find('table', {'class':'viewList'})
print(table)
trs = table.find_all('tr')
# print(len(trs))
cnt = 0
with open(os.path.join('data', 'webtoon.csv'), 'w', encoding='utf-8') as f:
# with open('data\\webtoon.csv', 'w', encoding='utf-8')) as f:
    for tr in trs:
        # print(imgurl)
        title = tr.find('a', {'id':'video-title'}).text
        # print(title)
        div = tr.find('div', {'class':'rating_type'})
        rating = div.find('strong').text
        # print(rating)
        regdate = tr.find('td', {'class':'num'}).text
        # print(regdate)
        str = '{}, {}, {}\n'.format(title, rating, regdate)
        f.write(str)