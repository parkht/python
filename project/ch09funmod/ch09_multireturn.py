def multi_return():
    return 100,200
def multi_return2():
    return 100,200,300


# main
a,b = 10,20
print(a,b)


# 2개의 리턴 값 2개의 변수에 각각 넣을 수 있다.
a, b = multi_return()
print(a,b)

a,b,c = 10,20,30
a, b, c = multi_return2()
print(a,b,c)