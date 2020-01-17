aa = [10, 20, 30, 40, 50]

# list aa의 값의 순서를 꺼꾸로 정렬하여 출력하시요.
aa = aa[::-1] # [50, 40, 30, 20, 10]

print(aa) # [50, 40, 30, 20, 10]

aa[2] = 300
print(aa) # [50, 40, 300, 20, 10]

# 1번째 500으로, 2번째는 400으로 변경
aa[0:2] = [500, 400]
print(aa) # [500, 400, 300, 20, 10]

#aa[0,3] = [550, 200]
#print(aa)

# aa list에서 1~2 데이터를 700 하나로 변경한다.
aa[1:3] = [700] # 결과값 [500, 700, 20, 10]
print(aa)

aa[1] = [1000,2000]
print(aa)
print(aa[0], type(aa[0])) # 500 <class 'int'>
print(aa[1], type(aa[1])) # [1000, 2000] <class 'list'>

# list의 데이터 삭제
aa[2:] = [] # [500, [1000, 2000]]
print(aa)


bb = [10,20,30,40,50,60,70]
bb[1], bb[4] = 200, 500
print(bb) # [10, 200, 30, 40, 500, 60, 70]

'''
aa[2] = [300, 350] # 결과값 : [50, 40, [300, 350], 20, 10]
print(aa)
aa[2:3] = [300, 350] # 결과값 : [50, 40, 300, 350, 20, 10]
print(aa)
'''

