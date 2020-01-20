# 1. 214.png 파일을 test.png로 다운로드 하기
# urllib 라이브러리를 사용
import urllib.request

# 다운로드 받아야할 url문자열 선언
# url = "http://uta.pw/shodou/img/28/214.png"
# 저장할 파일명 - 확장명은 같아야 한다. .png = .png
# savename = "test.png"

# 다운로드 실행
# urllib.request.urlretrieve(url, savename)
# print("저장되었습니다...!")

# 2. 다운로드 받고자하는 이미지 파일을 찾아서 다운로드 하기

url = "http://cafefiles.naver.net/20100704_260/kelly0029_1278199872306P2d8m_png/983121245_1257905494_kelly0029.png"
savename = "naver.png"

urllib.request.urlretrieve(url, savename)
print("저장 완료")