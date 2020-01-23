import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# 아이디와 비밀번호 지정하기
USER = 'parkht019'
PASS = 'parkht606060'

# 세션 시작하기
# post 방삭으로 통신을 위한 객체
session = requests.session()
# 로그인하기
# m_id, m_passwd는 hanbit.co.kr 사이트의 로그인 화면에서 form tag안의 input의 name에 맞춘다.
login_info = {
    "m_id" : USER,
    "m_passwd" : PASS
}
# post 방식으로 전달하고 form tag -> action 속성 값
# 아이디와 비빌번호를 받아서 로그인 처리를 해주는 프로그램(login_proc.php)
url_login = "http://www.hanbit.co.kr/member/login_proc.php"
res = session.post(url_login, data=login_info)
# status 확인 -> 200:정상, 그외 비정상 :404, 500 등
res.raise_for_status()

# 마이페이지에 접근하기
url_mypage = "http://www.hanbit.co.kr/myhanbit/myhanbit.html"
res = session.get(url_mypage)
res.raise_for_status()

# 마일리지와 이코인 가져오기
soup = BeautifulSoup(res.text, 'html.parser')
#print(soup)
mileage = soup.select_one(".mileage_section1 span").get_text()
ecoin = soup.select_one(".mileage_section2 span").get_text()
print("마일리지 :", mileage)
print("이코인 : ", ecoin)
