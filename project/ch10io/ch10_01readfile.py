import os

# 입력 텍스트파일 변수 선언
infp = None

# 한줄 단위로 텍스트 읽은 데이터 저장 변수
instr = ""

infn = input("파일명 입력 :")

# 파일명으로 존재하면 처리
if os.path.exists(infn):
    # 파일 읽기로 연결해서 사용
    # open(연결파일명, mode(r/w/+) r:읽기 w:쓰기 +:읽기쓰기
    infp = open(infn, "r")
    # 한줄 단위로 읽어와서 화면에 표시한다.
    while True:
        #  읽기
        instr = infp.readline()
        # 무한 while문을 빠져 나가는 조건 - 읽어 온 데이터가 없다.
        if not instr:
            break
        print(instr, end="")

    infp.close()
# 파일이 존재 하지 않는 경우 처리
else :
    print("파일이 존재하지 않습니다.")
