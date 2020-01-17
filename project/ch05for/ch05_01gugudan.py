# 구구단 처리를 하는데 시작 단수와 마지막 단수를 입력 받아서
# 시작단수 부터 마지막 단수 사이의 모든 단수를 출력한다.

start = int(input("시작 단수 :"))
end = int(input("끝 단수 :"))


for i in range(start, end+1):
    print(" ** %d단 ** " % i, end='')
for b in range(1,10):
    print('')
    for a in range(start,end+1):
        result = a * b
        print(" %d X %d =%2d " % (a, b, result),end='')


