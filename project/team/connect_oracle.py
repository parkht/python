#1. cx-oracle 다운로드 - pip 업데이트
#2. instantclient 다운로드 (https://www.oracle.com/database/technologies/instant-client/winx64-64-downloads.html)
#3. 다운로드 후 압축을 풀고 경로를 환경변수에 지정

#PATH = D:\instantclient;

#ORACLE_HOME = D:\instantclient

#TNS_ADMIN = D:\app\hong\virtual\product\12.2.0\dbhome_1\network\admin

#NLS_LANG = KOREAN_KOREA.KO16MSWIN949

#4. 연결
import cx_Oracle
import os
# 한글처리 import os  -> os.putenv('NLS_LANG','.UTF8')  ** 'UTF8' 입력시 'UTF-8'은 에러
os.putenv('NLS_LANG','.UTF8')

connection = cx_Oracle.connect("c##team1/team1@402-oracle:1521/orcl")
cur = connection.cursor()

sql = "select * from member"
sql2 = "insert into member(id,pw,name,birth,gender,tel,email,grade,bno) values ('testpython', 'qlalfqjsgh', '이름', '2020-01-02', " \
 "'남자', '010-0000-0000', 'dlapdlf@naver.com', 1, 0)"

cur.execute(sql2)
connection.commit()

cur.execute(sql)

for x in cur:
 print(x)

connection.close()
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# insert 구문 사용시
# connection.commit()
# 필요함.