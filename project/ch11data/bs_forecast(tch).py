from bs4 import BeautifulSoup
import urllib.request as req

def print_location_data(l):
    print("-------------- ", l.city.string, " ---------------")
    datas = l.find_all("data")
    for d in datas:
        print("일시 : ", d.tmef.string)
        print("날씨 : ", d.wf.string)
        print("최저온도 : ", d.tmn.string)
        print("최고온도 : ", d.tmx.string)


url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")
# print(soup)
title = soup.find("title").string
wf = soup.find("wf").string
print(title)
print(wf)

locations = soup.find_all("location")
# print(locations)
for l in locations:
    print_location_data(l)

print("\n\n\n\n************* 지역 날씨 찾기 *************")
sel_location = input("보고자 하는 지역을 입력하세요.")
for l in locations:
    if l.city.string == sel_location:
        print_location_data(l)
