# set : 중복된 데이터 배제 {v, v, v,.....}
mySet1 = {1,2,3,3,3,4,5,5,6,6,7}
print(mySet1, type(mySet1))  # {1, 2, 3, 4, 5, 6, 7} <class 'set'>

# list -> set -> list

salesList = ['삼각김밥', '바나나', '도시락', '삼각김밥', '삼각김밥', '도시락', '삼각김밥']
print(salesList)  # ['삼각김밥', '바나나', '도시락', '삼각김밥', '삼각김밥', '도시락', '삼각김밥']
print(set(salesList))  # {'삼각김밥', '도시락', '바나나'}

# 판매된 상품과 수량을 출력하시오. 중복이 되면 안된다.
for food in set(salesList):
    print("'%s'의 판매 수량 : %d" % (food, salesList.count(food)))

mySet2 = {1,2,3,4,5}
mySet3 = {4,5,6,7}
print('교집합 :' + str(mySet2 & mySet3))  # 교집합 :{4, 5}
print('합집합 :' + str(mySet2 | mySet3))  # 합집합 :{1, 2, 3, 4, 5, 6, 7}
print('차집합 :' + str(mySet2 - mySet3))  # 차집합 :{1, 2, 3}
print('대칭 차집합 :' + str(mySet2 ^ mySet3))  # 대칭 차집합 :{1, 2, 3, 6, 7}

num = [1,2,3,4,5]
num2 = []
for i in range(1,100+1):
    num2.append(i)
print('num2의 길이 :',len(num2)) # num2의 길이 : 100

# 컴프리헨션으로 리스트 만들기
num3 = [i for i in range(1,100+1)]
print('num3의 길이 :',len(num3)) # num3의 길이 : 100

# 1부터 100 사이의 3의 배수로 리스트 만들기
#for i in range(1, 100 + 1):
#    if i % 3 == 0:
#       num4.append(i)
num4 = [i for i in range(1,10+1) if i % 3 == 0]
print(num4)

# 1부터 10사이의 데이터를 제곱을 구해서 리스트 만들기
num5 = [i * i for i in range(1,10+1)]
print(num5)

foods = ['떡볶이','짜장면','라면','피자','맥주','치킨','삼겹살']
sides = ['오뎅','단무지','김치']
#for food, side in foods, sides :
for food, side in zip(foods, sides):
    print(food, '->', side)

for i in range(0, len(sides)):
    print(foods[i], '--->', sides[i])

for i in range(0, len(foods)):
    if(i < len(sides)):
        print(foods[i],'==>', sides[i])
    elif(i >= len(sides)):
        break

if len(foods) > len(sides):
    cnt = len(sides)
else:
    cnt = len(foods)
for i in range(cnt):
    print(foods[i], '===>', sides[i])

# zip함수를 이용해서 튜플 리스트, 딕셔너리 만들기
tupList = list(zip(foods,sides))
dic = dict(zip(foods,sides))
print('tupList :',tupList) # tupList : [('떡볶이', '오뎅'), ('짜장면', '단무지'), ('라면', '김치')]
print('dic :',dic) # dic : {'떡볶이': '오뎅', '짜장면': '단무지', '라면': '김치'}
