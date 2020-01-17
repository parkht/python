# 필요한 라이브러리 등록
import turtle
import random


## 함수 선언 부분
## 왼쪽 마우스 클릭 - 선을 그린다.
# 함수의 이름은 모두 소문자
# 포함 관계는 {}를 사용하지 않고 들여쓰기를 한다.
def screen_left_click(x, y):
    global r, g, b
    turtle.pencolor((r, g, b))
    turtle.pendown()
    turtle.goto(x, y)

## 오른쪽 마우스 버튼 - 이동만 선을 그리지 않는다.
def screen_right_click(x, y):
    turtle.penup()
    turtle.goto(x, y)

# 가운데 마우스 버튼 - 색상과 거북이 크기를 변환
def screen_mid_click(x, y):
    global r, g, b
    tSize = random.randrange(1, 10)
    turtle.shapesize(tSize)
    r = random.random()
    g = random.random()
    b = random.random()

# 변수 선언 부분
psize = 10
r, g, b = 0.0, 0.0, 0.0

# 메인 코드 부분
# 창이름
turtle.title('거북이로 그림 그리기')
# 그려질 포인터 형태 셋팅
turtle.shape('turtle')
# 선의 두께 셋팅
turtle.pensize(psize)

# onscreenclick - 클릭 이벤트 처리
# 1:마우스 왼쪽 버튼   2:마우스 가운데 버튼   3:마우스 오른쪽 버튼
turtle.onscreenclick(screen_left_click, 1)
turtle.onscreenclick(screen_mid_click, 2)
turtle.onscreenclick(screen_right_click, 3)

# 실행된 창을 유지 시킨다.
turtle.done()
