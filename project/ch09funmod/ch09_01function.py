# 전역변수
coffee = 0;


# 함수선언
def coffee_machine(button):
    print()
    # 물, 컵을 준비 -> 선택 불가능, 자동으로 한다.
    print('#1. (자동으로) 뜨거운 물을 준비힌다.')
    print('#2. (자동으로) 종이컵을 준비힌다.')
    print()

    # 버튼에 따라서 커피를 탄다.
    if button == 1:
        print("#3. (자동으로) 보통커피를 탄다.")
        coffee = '보통커피'
        return coffee
    elif button == 2:
        print("#3. (자동으로) 설탕커피를 탄다.")
        coffee = '설탕커피'
        return coffee
    elif button == 3:
        print("#3. (자동으로) 블랙커피를 탄다.")
        coffee = '블랙커피'
        return coffee
    else:
        print("#3. (자동으로) 아무거나 탄다.")
        coffee = '아무거나'
        return coffee
    print()


# 메인 부분
coffee = int(input('커피 선택(1.보통커피, 2.설탕커피, 3.블랙커피)'))
#기계가 커피를 탄다. -> 뒤에 것을 호출해서 오류가 없다.
coffee = coffee_machine(coffee)
# coffee_machine() -> 요구되어지는 매개변수의 값이 없다. 오류
# coffee_machine(coffee, coffee) -> 2번째 매개값이 있어서 오류

# 뒤에 것 coffee_machine(button)을 호출 하기 때문에 오류 -> 오버로드 x, 오버라이드 o

# 내준다.
print("손님 %s 나왔어요." % coffee)