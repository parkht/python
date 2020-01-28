from bs4 import BeautifulSoup
import urllib.request as req
import os.path

# xml 다운로드
url = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108'
savename = 'forecast.xml'
if not os.path.exists(savename):
    req.urlretrieve(url, savename)

# 다운로드 받은 파일을 읽기 전용으로 읽어 온다. -> 문자열
# BeautifulSoup로 분석하기
xml = open(savename, "r", encoding='utf-8').read()
# 구조로 가진 오브젝트로 만든다.
soup = BeautifulSoup(xml, 'html.parser')

#표시할 정보가 들어 있는 딕셔너리 데이터
# 각 지역 확인하기
info = {}
# 모든 지역의 데이터 찾기
for location in soup.find_all('location'):
    name = location.find('city').string
    weather = location.find('wf').string
    if not (weather in info):
        #     key     = value
        info[weather] = []
    info[weather].append(name)


print(info)  # {'맑음' : ['서울','인천','수원','파주',....]}
# 각 지역의 날시를 구분해서 출력하기
for weather in info.keys():
    print("+", weather)
    # 날씨에 해당되는 지역 리스트
    for name in info[weather]:
        print("| - ", name)