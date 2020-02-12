# 데코레이터 - 함수데코레이터, 클래스데코레이터
# def test(funciont):
#     return 'test 함수'
#
#
# @test
# def hello():
#     pass
#
# print(hello)
#
# # --------------------------------
# def test(f):
#     def inner():
#         print('start')
#         f()
#         print('end')
#     return inner
#
#
# @test
# def hello():
#     print('hello~~')
#
#
# hello()
#
# # ------------------------------------------
# class Test:
#     def __init__(self, function):
#         print('생성자 호출')
#         self.function = function
#     def __call__(self, *args, **kwargs):
#         print('start')
#         self.function()
#         print('end')
#
#
# @Test
# def hello():
#     print('hello~~')
#
#
# print('호출전')
# hello()
# print('호출후')

# ------------------------------------------
# 제너레이터
# 이터레이터 : next()함수를 사용해서 하나하나씩 꺼낼수 있는것
# a = [1, 2, 3, 4, 5, 6, 7]
# print(type(a))  # <class 'list'>
# ra = reversed(a)
# print(type(ra))  # <class 'list_reverseiterator'>
# print('ra :',ra)  # ra : <list_reverseiterator object at 0x000000AE7F8A0A58>
# print(next(ra))
# print(next(ra))
# print(next(ra))
# print(next(ra))
# print(next(ra))
# print(next(ra))
# print(next(ra))
# print(next(ra))  # error : iterator는 꺼낼 함수가 없을경우 에러를 발생
# for i in ra:
#     # print(next(i))  # TypeError: 'int' object is not an iterator
#     print(i)


# ------------------------------------------------------
# def test():
#     print('test 함수')
#     yield 'test'  # yield 키워드를 사용한 함수는 호출되도 사용이 안되고
#                   # next() 함수를 사용해야 호출된다.
#
#
# print('a')
# test()
#
# print('b')
# test()
# print(test())  # <generator object test at 0x000000F4FFE52990>

# --------------------------------------------------
# def test():
#     print('a')
#     yield 1
#     print('b')
#     yield 2
#     print('c')
#     yield 3
#
#
# output = test()
# k = next(output)
# print(k)
# k = next(output)
# print(k)
# k = next(k)

# ------------------------------------
# import pymysql as my
# # 1)db 연결
# conn = my.connect(host='localhost',
#                   user='tom',
#                   password='jerry',
#                   db='bookdb',
#                   charset='utf8',
#                   port=3307)
# # 2)커서생성
# cur = conn.cursor(my.cursors.DictCursor)
# # 3)쿼리문
# sql = 'select * from books_publisher'
# # 4)실행
# cur.execute(sql)
# rows = cur.fetchall()  # 데이터 전체에 접근하기
# print(type(rows))
# for row in rows:
#     # print(row[0], row[1], row[2], row[3])
#     print(row['id'], row['name'], row['address'], row['website'])
# # 5) 종료
# conn.close()

# ------------------------------------------------
# 데이터 입력
# import pymysql as my
# # 1)db 연결
# conn = my.connect(host='localhost',
#                   user='tom',
#                   password='jerry',
#                   db='bookdb',
#                   charset='utf8',
#                   port=3307)
# # 2)커서생성
# cur = conn.cursor(my.cursors.DictCursor)
# # 3)쿼리문
# sql = 'insert into books_publisher(name, address, website) values(%s, %s, %s)'
# # 4)실행
# cur.execute(sql,('경영', '서울시 구로구', 'iedu.or.kr'))
# conn.commit()
# # 5) 종료
# conn.close()

# ----------------------------------------------
# 수정
# import pymysql as my
# # 1)db 연결
# conn = my.connect(host='localhost',
#                   user='tom',
#                   password='jerry',
#                   db='bookdb',
#                   charset='utf8',
#                   port=3307)
# # 2)커서생성
# cur = conn.cursor(my.cursors.DictCursor)
# # 3)쿼리문
# sql = 'update books_publisher set address=%s, website=%s'
# # 4)실행
# # cur.execute(sql,('경영', '서울시 구로구', 'iedu.or.kr'))
# cur.execute(sql, ('서울시 구로구 구로동', 'web.co.kr'))
# conn.commit()
# # 5) 종료
# conn.close()

# --------------------------------------------------------
# 삭제
import pymysql as my
# 1)db 연결
conn = my.connect(host='localhost',
                  user='tom',
                  password='jerry',
                  db='bookdb',
                  charset='utf8',
                  port=3307)
# 2)커서생성
cur = conn.cursor(my.cursors.DictCursor)
# 3)쿼리문
sql = 'delete from books_publisher where id=%s'
# 4)실행
# cur.execute(sql,('경영', '서울시 구로구', 'iedu.or.kr'))
cur.execute(sql, (3))
conn.commit()
# 5) 종료
conn.close()