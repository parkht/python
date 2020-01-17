#print('\u2605')
'''

c=1
d=1
f=8
for i in range(1,10):
    if i < 6:
        for a in range(0,5-i):
            print(" ",end="")
            i += 1
        for b in range(0,c):
            print("\u2605",end="")
        c += 2
        print()
    elif i >= 6:
        for d in range(0,i-5):
            print(" ",end="")
            i += 1
        for e in range(1,f):
            print("\u2605",end="")
        f -= 2
        print()
'''
totalRow = 9
inc = 1
# blankcnt -> 4,3,2,1,0,1,2,3,4
# totalRow // 2 -> 4 ==> range(1, totalRow // 2 + 1)
# multi -> 절대값으로 만들어주는 변수
blankcnt, starcnt, multi = 4, 1, 1
for i in range(1, totalRow +1):
    #빈 공간을 출력
    blankcnt = ((totalRow // 2 + 1) - i) * multi
    # print(blankcnt)
    for j in range(1, blankcnt+1):
        print("  ", end ="")
    for k in range(1, starcnt+1):
        print("\u2605", end = "")
    print()
    starcnt += 2 * multi
    if i == totalRow // 2:
        multi = multi * -1

