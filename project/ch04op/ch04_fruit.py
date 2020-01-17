buy = input('먹고 싶은 과일은??')

fruit = ['사과','배','딸기','포도']
# print('과일 :',fruit)

fruit.append('귤')
# print(fruit)

if buy in fruit:
    print(buy,'가 있네요.^^')
else:
    print(buy,'가 없네요')