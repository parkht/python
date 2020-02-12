import datetime
now = datetime.date.today()
nowstring = now.strftime('%y-%m-%d')
print(nowstring)

import requests  # 특정웹사이트 접속
from bs4 import BeautifulSoup
import time


for page in range(1,3):
    time.sleep(1)
    pageurl = 'https://comic.naver.com/webtoon/list.nhn?titleId=570503&weekday=thu&page={}'
    url = pageurl.format(page)
    recvd = requests.get(url)
    # print(recvd)  # <Response [200]> 접속성공
    # print(recvd.text)  # html코드 확인
    dom = BeautifulSoup(recvd.text, 'lxml')  # lxml 파싱(잘못된 html 코드 수정)
    # 이미지저장, (제목, 별점 등록일) --> webtoon.csv 저장
    table = dom.find('table', {'class':'viewList'})
    # print(table)
    trs = table.find_all('tr')
    # print(len(trs))
    cnt = 0
    fn = 'd:\\git_hub\\python\\ml\\data\\' + nowstring + '.csv'
    # with open(os.path.join('data', 'webtoon.csv'), 'w', encoding='utf-8') as f:
    with open(fn, 'a', encoding='utf-8') as f:
        for tr in trs:
            if cnt == 0:
                cnt = cnt + 1
                continue
            imgurl = tr.find('img')['src']  # img태크의 속성을 찾는다.
            # print(imgurl)
            td = tr.find('td', {'class':'title'})
            title = td.find('a').text  # a태그의 텍스트를 찾는다.
            # print(title)
            # saveimg(imgurl, title)
            div = tr.find('div', {'class':'rating_type'})
            rating = div.find('strong').text
            # print(rating)
            regdate = tr.find('td', {'class':'num'}).text
            # print(regdate)
            str = '{}, {}, {}\n'.format(title, rating, regdate)
            f.write(str)


# pip install pyinstaller
# exe 실행파일 만들기
# pyinstaller -- noconsole -- onefile soup1.py