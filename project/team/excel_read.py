# File -> Settings -> Project : project -> Project Interpreter -> openpyxl 설치
import openpyxl

# 엑셀 파일 열기
# filename = 'stats_104102.xls'  #openpyxl.utils.exceptions.InvalidFileException: openpyxl does not support the old .xls file format
filename = 'stats_200129.xlsx'
book = openpyxl.load_workbook(filename)

# 맨 앞의 시트 추출하기
sheet = book.worksheets[0]

# 시트의 각 행을 순서대로 추출하기
data = []
for row in sheet.rows:
    data.append([
        row[0].value,
        row[9].value
    ])
print(data)
print(data[1][1])

data2 = []

for column in sheet.columns:
    data2.append([
        column[3].value
    ])
print('column : ',data2)

# 필요없는 줄(헤더, 연도, 계) 제거하기
del data[0]  # ['시도별 인구 변동 현황 [단위 : 천명]', None]
del data[0]  # [None, 2018]
del data[0]  # ['계', 51826]

print(data)
# 데이터를 인구 순서로 정렬합니다.
data = sorted(data, key=lambda x:x[1])
print('정렬 : ',data)

# 하위 5위를 출력합니다.
for i,a in enumerate(data):
    if(i >= 5 ): break
    print(i+1, a[0], int(a[1]))