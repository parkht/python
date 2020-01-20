import urllib.request

# url과 저장 경로 지정하기
url = "http://uta.pw/shodou/img/28/214.png"
savename ="test02.png"

# 다운로드
# 이미지 데이터 읽어오기
mem = urllib.request.urlopen(url).read()

# 파일로 저장하기
# with ~ as f: with문으로 선언된 객체는 with문 밖으로 나가면서 자동 소멸 close()된다.
# java --> try(자원 선언) try문 밖으로 나가면서 close()된다.
with open(savename, mode="wb") as f: # 'w'는 쓰기모드 'b'는 바이너리 모드
    f.write(mem) # write() : 다운로드한 바이너리 데이터를 파일에 저장
    print("저장되었습니다.")

url = "http://api.aoikujira.com/ip/ini"
res = urllib.request.urlopen(url)
data = res.read()

text = data.decode("utf-8")
print(text)