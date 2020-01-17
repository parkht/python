# list[]는 데이터 변경 가능, tuple()은 데이터 변경이 불가능
tt = (10,20,30)
print(tt, type(tt)) # (10, 20, 30) <class 'tuple'>

# tt.append(40) # AttributeError: 'tuple' object has no attribute 'append'
# print(tt, type(tt))

# tt[2] = 300 # TypeError: 'tuple' object does not support item assignment

# tt1 = tt.copy() # AttributeError: 'tuple' object has no attribute 'copy'
# print(tt1)

print(tt[0:2]) # (10, 20)

tt1 = tt
print(tt1 + tt) # (10, 20, 30, 10, 20, 30)
print(tt * 3) # (10, 20, 30, 10, 20, 30, 10, 20, 30) 3번 반복

# tuple -> list -> tuple 변경 가능

# tuple(10, 20, 30) -> list(10, 20, 30) -> list(10, 200, 300) -> tuple(10, 200, 300)
# tuple             -> list             -> 데이터 수정         -> tuple
tt = (10, 20, 30)
print('기본 데이터 :', tt,type(tt))
tl = list(tt)
tl.append(40)
tl[tt.index(20)] = 200
tt = tuple(tl)
print('변경된 데이터 :', tt, type(tt))










