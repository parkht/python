# a = [0, 0, 0, 0]
a = []
hap = 0

# a[0] = int(input('1번째 숫자 :'))

# print(a)

# print(a[0]) - 데이터가 없음 길이가 0
print(len(a))

for i in range(0, 4):
    a.append(int(input(str(i + 1)+"번째 숫자:")))

#for i in range(0, 4):
#    a[i] = int(input(str(i+1) + "번째 숫자 : "))

# a[0] = int(input('1번째 숫자 : '))
# a[1] = int(input('2번째 숫자 : '))
# a[2] = int(input('3번째 숫자 : '))
# a[3] = int(input('4번째 숫자 : '))


# 인덱스 값을 증가 시키면서 합계구함
# for i in range(0, len(a))
# hap = a[0] + a[1] + a[2] + a[3]
# print('합계 : %d' % hap)

aa=[]
# 리스트에 있는 데이터를 하나씩 꺼내와서 합계 구함
for i in a:
    hap += i

print('합계 : %d' % hap)

