import csv, codecs

# csv 파일 열기
filename = "list_euckr.csv"
fp = codecs.open(filename, 'r', 'utf-8')

# 한 줄씩 읽어 들이기
reader = csv.reader(fp, delimiter=",")
for cells in reader:
    print(cells[1], cells[2])