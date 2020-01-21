# html 구조화 시켜주는 라이브러리
from bs4 import BeautifulSoup
# 분석 데이터
html = """
<html><body>
  <h1>스크레이핑이란?</h1>
  <p>웹 페이지를 분석하는 것</p>
  <p>원하는 부분을 추출하는 것</p>
</body></html>
"""

# html 분석하기
# 분석하고자 하는 html 데이터를 BeautifulSoup(데이터, 작업모드) 파라미터를 넘긴다.
soup = BeautifulSoup(html, 'html.parser')

# soup에서 object 가져오기
# 원하는 부분 추출하기
# 위에서 하단으로 모든 단계를 다 선언해서 h1 찾기
h1 = soup.html.body.h1
# h2 = soup.h1 사용가능!! 구조와 상관없이 가장 처음에 있는 h1 찾기
h2 = soup.h1
p1 = soup.html.body.p
p2 = p1.next_sibling.next_sibling

# 요소의 글자 출력하기
print('h1 = ' + h1.string)
print('h2 = ' + h2.string)
print('p1 = ' + p1.string)
print('p2 = ' + p2.string)

for link in soup.find_all('p'):
    print('p = ' + link.string)