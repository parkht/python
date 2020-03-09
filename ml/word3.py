import os
import sys
import urllib.request
for i in range(1, 11):
    a = 1
    client_id = "hVv8LeNTyyMyn87KIYOL"
    client_secret = "ih0TigXoyF"
    encText = urllib.parse.quote("봄")
    url = "https://openapi.naver.com/v1/search/blog?start=",a,"&display=100&query=" + encText # json 결과
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
    a = a + 100
