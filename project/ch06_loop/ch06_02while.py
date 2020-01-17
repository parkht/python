# 1 ~ 10 까지 출력

i = 1

while i < 11:
    print(i,end="")
    i += 1
print()
# 1 부터 숫자를 계속 더한 숫자가 100보다 커지면 빠져나가서 출력

i = 1
sum = 0
while True:
    sum += i
    i += 1
    if sum > 100:
        break

print(sum)
# 1 ~ 10출력 홀수만 출력
# 1부터 시작하면서 2씩 중가
i = 1
while i < 11:
    print(i)
    i = i+2
# 짝수인 경우 출력하지 않고 반복처리를 계속 할 수 있도록 한다.
i = 0
while i < 11:
    # 만약에 짝수면 출력하지 않는다.
    if i % 2 == 0:
        i += 1  # 이게 없으면 무한 루프
        continue
    print('i는',i)
    i += 1
# 1부터 시작하면서 3의 나머지가 0 이면 continue
