# list
aa = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#      0,  1,  2,  3,  4,  5,  6,  7,  8,   9  배열 순서(+)
#    -10, -9, -8, -7, -6, -5, -4, -3, -2,  -1  배열 순서(-)
print("앞에서 두번째 데이터 : %d" % aa[1]) # 20
print("뒤에서 두번째 데이터 : %d" % aa[-2]) # 90

print("2번째 3번째 데이터" , aa[1:3]) # [20,30]
print("2번째 3번째 데이터의 타입", type(aa[1:3])) # <class 'list'>

print("1번째 부터 3번째 데이터", aa[0:3]) # [10, 20, 30]
print("1번째 부터 3번째 데이터", aa[:3]) # 처음부터 가져올 경우 앞의 0 생략가능

print("3번째부터 10번째 데이터", aa[2:10]) # [30,40,50,60,70,80,90,100]
print("3번째부터 10번째 데이터", aa[2:]) # 마지막까지 가져올 경우 10 생략가능

bb = aa[2:]
print(bb) # [0, 40, 50, 60, 70, 80, 90, 100]

# list 연산자 +, *
# 2개의 리스트를 합치자 aa, bb 합친다
print(aa+bb) #[10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 30, 40, 50, 60, 70, 80, 90, 100]
             #[                    aa                 ,              bb                ]
# 2개의 리스트 곱셈연산은 불가능 : print(aa * bb)

# 1개의 리스트 데이터를 3번 반복해서 데이터 만들기
print(aa*3) # list aa를 3번 반복







