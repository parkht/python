from selenium.webdriver import Firefox, FirefoxOptions

USER = ''
PASS = ''

# 파이어 폭스 실행
options = FirefoxOptions()
options.add_argument('-headless')
browser = Firefox(options=options)

# 로그인 페이지에 접근
url_login = 'https://nid.naver.com/nidlogin.login'
browser.get(url_login)
print('로그인 페이지에 접근합니다.')

# 텍스트박스에 아이디와 비밀번호 입력
e = browser.find_element_by_id('id')
e.clear()
e.send_keys(USER)
e = browser.find_element_by_id('pw')
e.clear()
e.send_keys(PASS)

# 입력 양식 전송해서 로그인
form = browser.find_element_by_css_selector('input.btn_global[type=submit]')
form.submit()
print("로그인 버튼을 클릭합니다.")

# 쇼핑 페이지의 데이터 가져오기
browser.get('http://order.pay.naver.com/home?tabMenu=SHOPPING')

# 쇼핑 목록 출력
products = browser.find_element_by_css_selector('.p_info span')
print(products)
for product in products:
    print('-', product.text)


