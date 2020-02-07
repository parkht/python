'''
def 함수명(매개변수):
    내용
'''


def hi():
    print('Hi~')


hi()


# sep='$' 구분기호를 '$'사용
def hi(name):
    print('Hi~', name, sep='$')


hi('kkk')  # Hi~$kkk

print('1. : ', hi('kkk'))  # Hi~$kkk
                           # 1. :  None


def hi(name):
    print('Hi~', name, sep='$')
    return 'ok'


print(hi('kkk'))  # Hi$kkk
                  # ok

def f1(x,y):
    r1 = x+y
    r2 = x-y
    r3 = x*y
    r4 = x/y
    return r1, r2, r3, r4


a, b, c, d = f1(10,3)
print(a, b, c, d)  # 13 7 30 3.3333333333333335
e = f1(30, 20)
print(e)  # (50, 10, 600, 1.5)
print(e[0])  # 50


def f2(x,y):
    r1 = x+y
    r2 = x-y
    r3 = x*y
    r4 = x/y
    return [r1, r2, r3, r4]


f = f2(50,30)
print(f)  #[80, 20, 1500, 1.6666666666666667]


def f3(x,y):
    r1 = x+y
    r2 = x-y
    r3 = x*y
    r4 = x/y
    return {'add':r1, 'sub':r2, 'mul':r3, 'div':r4}


g = f3(20,10)
print(g)  # {'add': 30, 'sub': 10, 'mul': 200, 'div': 2.0}
print(g['add'])  # 30


def f4(*a):
    print(type(a), end='  ')
    print(a, end='  ')
    hap = 0
    for i in a:
        hap = hap + i
    print('총합 :', hap)


f4(1,2,3)  # <class 'tuple'>  (1, 2, 3)  총합 : 6


def f5(**b):
    print(type(b), end='  ')
    print(b)


# f5(4,2)  # error : f5() takes 0 positional arguments but 2 were given
f5(name1=['둘리', '철수'], name2='희동이')  # <class 'dict'>  {'name1': '둘리', 'name2': '희동이'}


def f6(a, b, *c, **d):  # def f6(*a, **b, c, d): => error
    print(a, b, c, d)


f6(1, 2, 3, 4, 5, 6)  # 1 2 (3, 4, 5, 6) {}
f6(1, 2)  # 1 2 () {}
# f6(1)  # error : f6() missing 1 required positional argument: 'b'
f6(1, 2, apple='red', name='김길동')  # 1 2 () {'apple': 'red', 'name': '김길동'}


def f7(a, b=2, c=3, d=4):  # def f7(a=1, b=2, c=3, d): => error
    print(a, b, c, d)


# f7()  # error : f7() missing 1 required positional argument: 'a'
f7(5, 6)  # 5 6 3 4
f7(5, d=6)  # 5 2 3 6

# -------------------------------------------------
# 컴프리핸션
a = [1, 2, 3, 4, 5]
print(a)

a=[]
for i in range(1, 11):
    print(i, end=' ')
    a.append(i)
print('a :', a)

b = [n for n in range(1, 11)]  # 컴프리핸션
print('b :', b)

c = []
for i in range(100):
    c.append(7)
print(c)

d = [7 for i in range(100)]  # 컴프리핸션
print(d)

e = []
for i in range(1, 101):
    if i%2 == 1:
        e.append(i)
print(e)

f = [i for i in range(1, 101) if i%2 == 1]  # 컴프리핸션
print(f)

g = 'tensorflow'
for c in g:
    print(c, end='   ')  # t   e   n   s   o   r   f   l   o   w
print()
h = [c for c in g]
print(h)  # ['t', 'e', 'n', 's', 'o', 'r', 'f', 'l', 'o', 'w']
i = {c:0 for c in g}
print(i)  # {'t': 0, 'e': 0, 'n': 0, 's': 0, 'o': 0, 'r': 0, 'f': 0, 'l': 0, 'w': 0}
for c in enumerate(g):
    print(c, end='')  # (0, 't')(1, 'e')(2, 'n')(3, 's')(4, 'o')(5, 'r')(6, 'f')(7, 'l')(8, 'o')(9, 'w')
print()

for i,c in enumerate(g):
    print(i, c, end="&")  #0 t&1 e&2 n&3 s&4 o&5 r&6 f&7 l&8 o&9 w&
print()
d = {i:c for i,c in enumerate(g)}
print(d)  # {0: 't', 1: 'e', 2: 'n', 3: 's', 4: 'o', 5: 'r', 6: 'f', 7: 'l', 8: 'o', 9: 'w'}

# ---------------------------------------------------------------
import json
j1 = '{"ip":"8.8.8.8"}'
print(j1)  # {"ip":"8.8.8.8"}
print(type(j1))  # <class 'str'>
d1 = json.loads(j1)  # 문자열 -> dict,  json.load() : 파일 -> dict
print(d1)  # {'ip': '8.8.8.8'}
print(type(d1))  # <class 'dict'>
print(d1['ip'])  # 8.8.8.8

j2 = '''{
   "Accept-Language": "en-US,en;q=0.8",
   "1004": false,
   "hobby": null,
   "Host": "headers.jsontest.com",
   "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
}'''
print(j2)
print(type(j2))  # <class 'str'>
d2 = json.loads(j2)
print(d2)
print(type(d2))  # <class 'dict'>

print('-'*30)
jj2 = json.dumps(d2)  # dict -> 문자열
print(jj2)
print(type(jj2))  # <class 'str'>






