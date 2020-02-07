# 네이버 Papago NMT API 예제
import json
import os
import sys
import urllib.request
client_id = "JtcGUf64gsBIKWjyMTye"
client_secret = "yt0Oyfk1_q"
encText = urllib.parse.quote("어제는 우박이 내렸어요")
data = "source=ko&target=en&text=" + encText
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    result = response_body.decode('utf-8')
else:
    print("Error Code:" + rescode)

tojson = json.loads(result)
print(tojson['message'])
message = tojson['message']
print(message)
result = message['result']
print(result)
translatedText = result['translatedText']
print(translatedText)

# translatedText의 value를 얻기 위한 과정
translatedText = tojson['message']['result']['translatedText']


