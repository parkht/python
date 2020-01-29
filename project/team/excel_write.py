import openpyxl

# 엑셀 파일 열기
filename = 'stats_200129.xlsx'
book = openpyxl.load_workbook(filename)

# 활성화된 시트 추출하기
sheet = book.active
print(sheet[str(chr(66))+'3'].value)
print(str(chr(65)))  # chr(65) -> A
# 서울을 제외한 인구를 구해서 쓰기
for i in range(0,9):
    total = int(sheet[str(chr(i+66))+'3'].value)
    #                        B열    +3행
    seoul = int(sheet[str(chr(i+66))+'4'].value)
    #                        B열    +4행
    output = total - seoul
    print('서울 제외 인구 = ', output)
    # 쓰기
    sheet[str(chr(i+66))+'21'] = output
    cell = sheet[str(chr(i+66))+'21']
    # 폰트와 색상 변경해보기
    cell.font = openpyxl.styles.Font(size=12,color='FF0000')
    cell.number_format = cell.number_format

# 엑셀 파일 저장하기
filename = 'population.xlsx'
book.save(filename)
print('OK')