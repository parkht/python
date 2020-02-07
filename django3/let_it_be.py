import json
import os
import sys
import urllib.request
client_id = "JtcGUf64gsBIKWjyMTye"
client_secret = "yt0Oyfk1_q"
text = open('data\\song.txt').read()
encText = urllib.parse.quote(text)
data = "source=en&target=ko&text=" + encText
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
print(tojson)

