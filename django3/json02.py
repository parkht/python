# import os
# import sys
# import urllib.request
# import json
# client_id = "Sx5B1S4vxKw63EXAkb1R"
# client_secret = "WQHWdxoQTb"
# encText = urllib.parse.quote("코로나")
# url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
# request = urllib.request.Request(url)
# request.add_header("X-Naver-Client-Id",client_id)
# request.add_header("X-Naver-Client-Secret",client_secret)
# response = urllib.request.urlopen(request)
# rescode = response.getcode()
# if(rescode==200):
#     response_body = response.read()
#     result = response_body.decode('utf-8')
# else:
#     print("Error Code:" + rescode)
# tojson = json.loads(result)
# # print(tojson)
# # print(type(tojson))
# # print(tojson['items'])
#
# for dic in tojson['items']:
#     title = dic['title']
#     description = dic['description']
#     title = title.replace('<b>코로나</b>', '코로나')
#     title = title.replace(',', ' ')
#     description = description.replace('<b>코로나</b>', '코로나')
#     description = description.replace(',', ' ')
#
#     print(title)
#     print(description)
#     print('-'*30)

# -------------------------------------------------------------------
# 정제한 정보 => 파일저장
import os
import sys
import urllib.request
import json
client_id = "Sx5B1S4vxKw63EXAkb1R"
client_secret = "WQHWdxoQTb"
encText = urllib.parse.quote("코로나")
url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
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

with open('data\\corona.csv', 'w', encoding='utf-8') as f:
    tojson = json.loads(result)
    for dic in tojson['items']:
        title = dic['title']
        description = dic['description']
        title = title.replace('<b>코로나</b>', '코로나')
        title = title.replace(',', ' ')
        description = description.replace('<b>코로나</b>', '코로나')
        description = description.replace(',', ' ')
        str = title + ',' + description + '\n'
        f.write(str)
