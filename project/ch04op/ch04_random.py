import turtle
import random


# 전역변수 선언부분
swidth, sheight, pSize, exitCount = 300, 300, 3, 0
r, g, b, angle, dist, curX, curY = [0] * 7


# 메인 코드 부분
# 거북이의 세팅부분
turtle.title('거북이가 맘대로 ??!!')
turtle.shape('turtle')  # 거북이 모양 불러오기
turtle.pensize(pSize)
# width, height는 변수가 아니고 setup에서 사용하는 속성이다.
turtle.setup(width = swidth + 30, height = sheight + 30)
turtle.screensize(swidth, sheight)

# 무한 반복 -> break전까지 -> if문을 이용해서 조건에 맞으면 빠져 나간다.
while True:
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.pencolor(r, g, b)

    angle = random.randrange(0, 360)
    dist = random.randrange(1, 100)
    turtle.left(angle)
    turtle.forward(dist)
    curX = turtle.xcor()
    curY = turtle.ycor()

    if(-swidth / 2 <= curX and curX <= swidth / 2) and (-sheight /2 <= curY and curY<= sheight / 2):
        pass
    else:
        turtle.penup()
        turtle.goto(0,0)
        turtle.pendown()

        exitCount +=1
        if exitCount >=5 :
            break

turtle.done()
