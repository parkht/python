import random

# 변수
num = 0
numList = []
while True:
    num = random.randrange(1,46)
    numList.append(num)
    numList = set(numList)
    numList = list(numList)
    if len(numList) >= 6:
        break

print(numList)

