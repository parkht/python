# 함수 선언
def my_func():
    print('함수 호출')


# 전역변수
gvar = 100


# 메인 코드 부분
#if __name__ == '__main__':
# main()만 선언을 한 경우는 시작부분으로 인정하지 않는다.
# 함수 선언 없이 처리문을 만들거나 if __name__ 선언해서 main을 호출
def main():
    print('메인 함수 부분이 실행됩니다.')
    my_func()
    print('전역 변수 gvar:', gvar)


#if __name__ == '__main__':
#    print("여기부터~")
#    main()
main()
