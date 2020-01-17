# dictionary -> {key : value, key: value ....} -> js : json 형식
dic1 = {1: 'a', 2: 'b', 3: 'c'}
print(dic1,type(dic1)) # {1: 'a', 2: 'b', 3: 'c'} <class 'dict'>

# key값이 같으면 앞의 데이터를 뒤의 데이터가 덮어쓰기가 된다.
dic1 = {1: 'a', 2: 'b', 3: 'c', 3: 'd'}
print(dic1) # {1: 'a', 2: 'b', 3: 'd'}

# 학생 딕셔너리 생성
student1 = {'학번': 1000, '이름': '홍길동', '학과': '파이썬학과', '학번': 2000}
print(student1, type(student1)) # {'학번': 2000, '이름': '홍길동', '학과': '파이썬학과'} <class 'dict'>

# 학생의 이름 데이터 가져오기
print(student1['이름']) # 홍길동
print(student1.get('이름')) # 홍길동
# 모든 key를 출력해 보자
keylist = student1.keys()
print(student1.keys()) # dict_keys(['학번', '이름', '학과'])

keylist1 = list(student1.keys())
print(keylist1) # ['학번', '이름', '학과'] key 값을 list로 변환

valuelist = student1.values()
print(valuelist) # dict_values([2000, '홍길동', '파이썬학과'])

# 학생딕셔너리가 가지고 있는 모든 데이터 출력해 보기
for a in keylist:
    print(a, ':', student1[a])
# 학번 : 2000
# 이름 : 홍길동
# 학과 : 파이썬학과

print(student1.items()) # dict_items([('학번', 2000), ('이름', '홍길동'), ('학과', '파이썬학과')])

student1list = list(student1.items())
print(student1list) # [('학번', 2000), ('이름', '홍길동'), ('학과', '파이썬학과')]
print(type(student1list)) # <class 'list'>

student1list.append(('연락처','010-1122-3355'))
print(student1list) # [('학번', 2000), ('이름', '홍길동'), ('학과', '파이썬학과'), ('연락처', '010-1122-3355')]

print(student1list.pop()) # ('연락처', '010-1122-3355')

print(student1list) # [('학번', 2000), ('이름', '홍길동'), ('학과', '파이썬학과')]

student1list.append(('이름','김길동'))
print(student1list) # [('학번', 2000), ('이름', '홍길동'), ('학과', '파이썬학과'), ('이름', '김길동')]

# 딕셔너리의 데이터 추가
singer = {}
singer['이름'] = '트와이스' # 비교 : 자바스크립드 singer.이름 = '트와이스'
singer['구성원수'] = 9
# 같은 'key'를 사용해서 데이터를 넣으면 수정이 된다.
singer['구성원수'] = 10
singer['대표곡'] = '히든'
singer['데뷔'] = '서바이벌 식스틴'

print(singer) # {'이름': '트와이스', '구성원수': 10, '대표곡': '히든', '데뷔': '서바이벌 식스틴'}

# singer 딕셔너리 '대표곡' 항목을 삭제
del singer['대표곡']

print(singer) # {'이름': '트와이스', '구성원수': 10, '데뷔': '서바이벌 식스틴'}



