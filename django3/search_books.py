import os
import sys
import urllib.request
import json
import requests


def saveimg(title, image):
    filename = os.path.join('img2', title + image[-27:-23])
    # print(filename)
    recvdimg = requests.get(image)
    f = open(filename, 'wb')
    f.write(recvdimg.content)


client_id = "Sx5B1S4vxKw63EXAkb1R"
client_secret = "WQHWdxoQTb"
encText = urllib.parse.quote("파이썬")
# url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
url = "https://openapi.naver.com/v1/search/book.json?query=" + encText + "&display=100" # 책 검색
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    result = response_body.decode('utf-8')
else:
    print("Error Code:" + rescode)

# 책 제목, 저자, 출판사, 가격 => data\\book.csv

with open('data\\books.csv', 'w', encoding='utf-8') as f:
    tojson = json.loads(result)
    for dic in tojson['items']:
        title = dic['title']
        author = dic['author']
        publisher = dic['publisher']
        price = dic['price']
        image = dic['image']
        title = title.replace('<b>파이썬</b>', '파이썬')
        title = title.replace(',', ' ')
        title = title.replace('/', '')
        saveimg(title, image)
        author = author.replace('|', ' ')
        # print('{},{},{},{},{}'.format(title, image, author, publisher, price))
        str = '{},{},{},{},{}\n'.format(title, image, author, publisher, price)
        f.write(str)


