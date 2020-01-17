money = int(input('교환할 돈은 얼마인가요??'))
print("")
'''
a = money//500
print('500원 짜리 :', a,'개')
b = (money%500)//100
print('100원 짜리 :',b,'개')
c = ((money%500)%100)//50
print('50원 짜리 :', c,'개')
d = (((money%500)%100)%50)//10
print('10원 짜리 :', d,'개')
e = (((money%500)%100)%50)%10
print('바꾸지 못한 잔돈 :', e,'원')
'''


def calcu(a, money):
    # 바꿔야할 돈의 갯수
    cnt = money // a
    print(a,'원의 갯수 :',cnt)
    # 남아있는 지급된 돈
    money = money % a
    return money


ch_money = 500
money = calcu(ch_money, money)

ch_money = 100
money = calcu(ch_money, money)

ch_money = 50
money = calcu(ch_money, money)

ch_money = 10
money = calcu(ch_money, money)

print('최종잔액', money)
