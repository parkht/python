import codecs

# euc_kr로 저장된 csv 파일 읽기
filename = "list_euckr.csv"
csv = codecs.open(filename, 'r', 'utf-8').read()

# csv을 파이썬 리스트로 변환하기
data = []
rows = csv.split("\r\n")
for row in rows:
    if row == "": continue
    cells = row.split(",")
    data.append(cells)

for c in data:
    print(c[1],c[2])