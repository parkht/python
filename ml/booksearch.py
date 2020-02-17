import os
import sys
import urllib.request
import json
import pandas as pd
client_id = "hVv8LeNTyyMyn87KIYOL"
client_secret = "ih0TigXoyF"
encText = urllib.parse.quote("파이썬")
url = "https://openapi.naver.com/v1/search/book.json?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    data = response_body.decode('utf-8')
else:
    print("Error Code:" + rescode)

data = json.loads(data)
# print(type(data))
print(data['items'])
col = ['title', 'publisher', 'price', 'author', 'pubdate']

df = pd.DataFrame(data['items'], columns=col)
print(df)
df.to_csv('data/books.csv', sep=' ', index=False)

