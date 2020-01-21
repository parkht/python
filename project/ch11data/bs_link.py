from bs4 import BeautifulSoup

html = """
<html>
<body>
  <ul>
    <li><a href='http://www.nvar.com'>naver</a></li>
    <li><a href='http://www.daum.net'>daum</a></li>
  </ul>
</body>
</html>
"""
# 데이터로 활용하기 위해서
linklist = []


# html 분석하기
soup = BeautifulSoup(html, 'html.parser')

# a 태그의 데이터가 여러개 이므로
# find() : 한개 찾기, find_all(): 모두찾기 -> find_all() 이용한다.
# find() -> object,  find_all() -> [object, ...] : list
links = soup.find_all('a')
print(links)  #  links 데이터 확인 : list로 나온다.
# 링크 목록 출력하기
for a in links:
    # 데이터 한개를 가져오면 딕셔너리로 저장 -> ({site:값, url:값},{...})
    data = {}
    href = a.attrs['href']
    text = a.string
    print(text, '>>' ,href)
    # 딕셔너리에 데이터 추가
    data['site'] = text
    data['url'] = href
    # 리스트에 딕셔너리 추가
    linklist.append(data)

print(linklist)