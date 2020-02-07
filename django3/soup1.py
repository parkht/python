# https://www.naver.com/robots.txt
# 특정 사이트의 접근제한 정책 확인

# 포멧팅
# print('{} + {} = {}'.format(3, 4, 3+4))  # 3 + 4 = 7
# print('{0} + {1} = {1}'.format(3, 4, 3+4))  # 3 + 4 = 4
# print('%d + %d = %d'%(3, 4, 3+4))  # 3 + 4 = 7
# print('%s + %s = %s'%('3', 4, 3+4))  # 3 + 4 = 7
# print('%d + %s = %s'%('a', 4, 3+4))  # TypeError: %d format: a number is required, not str
# print('%0.4f'%(3.141592))  # 3.1416

# -----------------------------------------------
# import os
#
# import requests  # 특정웹사이트 접속
# from bs4 import BeautifulSoup
#
#
# def saveimg(imgurl, title):
#     # print(imgurl[-4:])
#     title = title.replace(':', '')
#     title = title.replace('<', '')
#     title = title.replace('>', '')
#     filename = os.path.join('img', title + imgurl[-4:])
#     # print(filename)
#     recvdimg = requests.get(imgurl)
#     f = open(filename, 'wb')
#     f.write(recvdimg.content)
#
#
# url = 'https://comic.naver.com/webtoon/list.nhn?titleId=570503&weekday=thu'
# recvd = requests.get(url)
# # print(recvd)  # <Response [200]> 접속성공
# # print(recvd.text)  # html코드 확인
# dom = BeautifulSoup(recvd.text, 'lxml')  # lxml 파싱(잘못된 html 코드 수정)
# # 이미지저장, (제목, 별점 등록일) --> webtoon.csv 저장
# table = dom.find('table', {'class':'viewList'})
# # print(table)
# trs = table.find_all('tr')
# # print(len(trs))
# cnt = 0
# with open(os.path.join('data', 'webtoon.csv'), 'w', encoding='utf-8') as f:
# # with open('data\\webtoon.csv', 'w', encoding='utf-8')) as f:
#     for tr in trs:
#         if cnt == 0:
#             cnt = cnt + 1
#             continue
#         imgurl = tr.find('img')['src']  # img태크의 속성을 찾는다.
#         # print(imgurl)
#         td = tr.find('td', {'class':'title'})
#         title = td.find('a').text  # a태그의 텍스트를 찾는다.
#         # print(title)
#         saveimg(imgurl, title)
#         div = tr.find('div', {'class':'rating_type'})
#         rating = div.find('strong').text
#         # print(rating)
#         regdate = tr.find('td', {'class':'num'}).text
#         # print(regdate)
#         str = '{}, {}, {}\n'.format(title, rating, regdate)
#         f.write(str)

# -----------------------------------------------------------------
import os

import requests  # 특정웹사이트 접속
from bs4 import BeautifulSoup
import time


def saveimg(imgurl, title):
    # print(imgurl[-4:])
    title = title.replace(':', '')
    title = title.replace('<', '')
    title = title.replace('>', '')
    filename = os.path.join('img', title + imgurl[-4:])
    # print(filename)
    recvdimg = requests.get(imgurl)
    f = open(filename, 'wb')
    f.write(recvdimg.content)

for page in range(1,6):
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
    with open(os.path.join('data', 'webtoon.csv'), 'w', encoding='utf-8') as f:
    # with open('data\\webtoon.csv', 'w', encoding='utf-8')) as f:
        for tr in trs:
            if cnt == 0:
                cnt = cnt + 1
                continue
            imgurl = tr.find('img')['src']  # img태크의 속성을 찾는다.
            # print(imgurl)
            td = tr.find('td', {'class':'title'})
            title = td.find('a').text  # a태그의 텍스트를 찾는다.
            # print(title)
            saveimg(imgurl, title)
            div = tr.find('div', {'class':'rating_type'})
            rating = div.find('strong').text
            # print(rating)
            regdate = tr.find('td', {'class':'num'}).text
            # print(regdate)
            str = '{}, {}, {}\n'.format(title, rating, regdate)
            f.write(str)

