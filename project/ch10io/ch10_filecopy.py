import os

infp = None

instr = ""

infn = input("복사할 파일명 :")

if os.path.exists(infn):
    # 파일 읽기로 연결해서 사용
    # open(연결파일명, mode(r/w/+) r:읽기 w:쓰기 +:읽기쓰기
    infp = open(infn, "r")
    # 한줄 단위로 읽어와서 화면에 표시한다.
    # 읽기
    instr = infp.read() # 전체를 읽을땐 read()
        # 무한 while문을 빠져 나가는 조건 - 읽어 온 데이터가 없다.
    print(instr, end="")
    print()

outfn = input("복사된 파일명 :")

if os.path.exists(outfn):
    print("파일명이 존재 합니다.")

else:
    outfp = open(outfn, "w", encoding="UTF-8")

    outfp.writelines(instr)

outfp.close()

infp.close()
# 파일이 존재 하지 않는 경우 처리