# 파이썬 메뉴얼을 재귀적으로 다운받는 프로그램
# 모듈 읽어 들이기
from bs4 import BeautifulSoup
from urllib.request import *
from urllib.parse import *
from os import makedirs
import os.path, time, re

# 이미 처리한 파일인지 확인하기 위한 변수
# 다운로드 받은 레이지 저장
proc_files = {}

# html 내부에 있는 링크를 추출하는 함수
# enum_links(분석해야할 html 문서, 다운로드 받은 페이지)
def enum_links(html, base):
    soup = BeautifulSoup(html, 'html.parser')
    # CSS 링크 추가 -> 객체 리스트
    links = soup.select("link[rel='stylesheet']")  # CSS
    # a 링크 추가 -> 위의 객체 리스트에 리스트를 추가
    links += soup.select("a[href]")  # 링크
    # 링크 페이지(links:태그)를 절대 주소로 받아서 추가 시키는 리스트
    result = []
    #  href 속성을 추출하고, 링크를 절대 경로로 변환
    for a in links:
        # 링크 걸린 url을 가져오기
        href = a.attrs['href']
        # 가져온 url를 절대 주소로 변환
        url = urljoin(base, href)
        # result에 추가 -> 가져와야할 페이지 저장
        result.append(url)
    return result


# 파일을 다운받고 저장하는 함수
# url은 다운로드 받아야할 절대 페이지
def download_file(url):
    o = urlparse(url)
    # savepath => 내 컴퓨터의 위치를 정한다. -> 파일 포함
    # "./" -> 실행되고 있는 현재 -> ch12cookie/
    # o.netloc -> 서버의 위치(docs.python.org)
    # o.path -> 서버 뒤에 있는 내용
    savepath = './' + o.netloc + o.path
    # savepath의 내용이 "/"로 끝나면 페이지가 없다. -> 기본페이지(index.html) 추가
    if re.search(r"/$", savepath):  # 폴더라면 index.html
        savepath += "index.html"
    # 저장 폴더가 있는지 확인하기 위해서 폴더를 찾아낸다
    savedir = os.path.dirname(savepath)
    # 폴더가 존재하면 이미 처리한 것으로 추정해서 바로 리턴한다.
    # 모두 다운됐는지 확인
    if os.path.exists(savepath):return savepath
    # 폴더가 존재하지 않으면 폴더를 만들고 다운로드를 실행한다.
    # 다운받을 폴더 생성
    if not os.path.exists(savedir):
        print("mkdir=", savedir)
        makedirs(savedir)
    # 파일 다운받기
    try:
        print('download=', url)
        # 다운로드 실행
        urlretrieve(url, savepath)
        # 다운로드된 페이지 이름을 출력하는 것을 확인하기 위해 1초간 딜레이
        time.sleep(1)  # 1초 딜레이
        return savepath
    except:
        print("다운 실패 :", url)
        return None


# html 분석하고 다운받는 함수 analyze_html(분석하려는 페이지, base)
def analyze_html(url, root_url):
    # 분석하려는 페이지 -> download_file()다운로드 받는다. : 처음에는 기본 페이지 다운
    savepath = download_file(url)
    # 다운로드 받은 페이지가 None 이다 -> 다운로드를 받았다라는 의미
    if savepath is None : return
    if savepath in proc_files: return   # 이미 처리되었다면 실행하지 않음
    # proc_files -> 다운받은 페이지를 key로 해서 저장한다.
    proc_files[savepath] = True
    # 다운로드 받는 페이지 분석
    print("analyze_html = ", url)
    # html로 읽어 오기 -> 다운로드된 파일을 읽기 전용으로 열고 전체를 읽어온다.
    # 링크 추출
    html = open(savepath, 'r', encoding='utf-8').read()
    # 다운로드 받은 페이지에 링크가 걸려있는 목록을 가져온다. enum_links()호출
    links = enum_links(html, url)

    for link_url in links :
        #링크 루트 이외의 경로를 나타낸다면 무시
        # link_url.find(root_url) !=0 -> link_url이 root_url로 시작하지 않는다.
        if link_url.find(root_url) !=0:
            # r".css$" => .css로 끝난다.
            # link_url이 .css로 끝나지 않는다.(앞에 not이 있으므로) -> css파일이 아니다.
            if not re.search(r".css$", link_url):continue
        # link)url의 페이지가 html 또는 htm 으로 끝나면 다시 링크를 분석해야한다.
        if re.search(r".(html|htm)$", link_url):
            # 재귀적으로 html 파일 분석하기
            # 다운로드 받은 페이지가 html이나 htm 경우 다시 분석 실행
            analyze_html(link_url, root_url)
            continue
        # 기타파일
        # link_url가 html이나 htm이 아니고 다른 사이트의 url이 아닌 경우
        # 예) 이미지 링크 => 같은 경우 - 다운로드
        download_file(link_url)


# 시작되는 부분
if __name__ == '__main__':
    # 다운로드 받고자 하는 기본 페이지
    # url에 있는 모든 것 다운받기
    url = "https://docs.python.org/3.8/library/"
    # 페이지 분석 -> 기본페이지 분석 -> link를 리스트로 만든다. -> 다운받는다.
    analyze_html(url, url)

