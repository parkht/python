aa = [85, 100, 90, 70, 95, 90]

# 1.리스트의 갯수를 출력
print('aa 리스트의 갯수 :',len(aa))
# 2.리스트의 데이터 바꾸지 않으면서 정렬해서 출력
aa1 = sorted(aa)
print('aa1리스트의 정렬 :',aa1)
print('aa리스트 :', aa)
# 3.'90'데이터의 위치를 출력
# aa.index(값[, 시작번호[, 끝번호]])
print('90의 위치 :',aa.index(90))
# 4.마지막 데이터를 꺼내면서 제거해 보세요
i = aa.pop()
print('지워진 값 : ',i)
print('마지막 데이터를 지운 aa :', aa)
# 5.'bb'라는 리스트에 동일한 데이터를 가지도록 처리해보세요
bb = aa.copy()
print('리스트 bb :',bb)
# 6.'aa' 리스트의 값이 100인 데이터를 지운다. aa.remove(100)
a2 = int(input("지울값을 적으세요:"))
a1 = aa.index(a2)
print('%d의 위치 : %d'%(a2,aa.index(a2)))
del(aa[a1])
print('%d을 지운 aa: %s ' % (a2, aa))
# 7. 'aa' 리스트의 전체 내용 지운다.
aa.clear()
print('모든 값을 지운 aa:',aa)
