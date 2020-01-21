import urllib.request
import urllib.parse
f =""
API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
# 매개변수를 URL 인코딩 합니다.
# 전국(108),서울/경기(109),강원도(105)
values = {
    'stnId':'109'
}
# key:value & key:value ... --->query(JSON형식)
params = urllib.parse.urlencode(values)
# 요청 전용 URL을 생성합니다.
url = API + '?' + params
print('url=',url)
# 다운로드 합니다.
data = urllib.request.urlopen(url).read()
text = data.decode('utf-8')  # 읽어온 데이터를 한글처리 decode('utf-8')
savename = 'test2.xml'

f = open(savename, 'w', encoding='utf-8')

f.write(text)

f.close()

print(text)