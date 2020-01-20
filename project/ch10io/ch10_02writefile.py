import os

outfp = None

# 출력할 파일명 입력
outfn = input("출력할 파일명 입력 :")

# 파일 객체를 쓰기로 열기
outfp = open(outfn, "w", encoding="UTF-8")

instr = ""

# 글자를 입력하는 대로 출력하기를 한다.
while True:
    instr = input("텍스트 입력 :")
    # 빠져나갈 조건 -> 아무것도 안하고 엔터를 누른다.
    if not instr:
        break
    outfp.writelines(instr)

outfp.close()