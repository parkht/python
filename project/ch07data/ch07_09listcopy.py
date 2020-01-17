# 별개의 새로운 리스트를 만든다. 예전에 데이터를 그대로 사용
oldList = ['짜장면']
newList = oldList

print('oldList :', oldList) # ['짜장면']
print('newList :', newList) # ['짜장면']

oldList.append('탕수육')
print("oldlist : ", oldList) # ['짜장면', '탕수육']
print("newlist : ", newList) # ['짜장면', '탕수육']

newList.append('군만두')
print("oldlist : ", oldList) # ['짜장면', '탕수육', '군만두']
print("newlist : ", newList) # ['짜장면', '탕수육', '군만두']

# 별개로 동작 데이터 복사
newList = oldList.copy()
newList.append('짬뽕')
print(oldList) # ['짜장면', '탕수육', '군만두']
print(newList) # ['짜장면', '탕수육', '군만두', '짬뽕']

newList = oldList[:]
oldList.append('울면')
print(oldList)
print(newList)

newList=[]
for data in oldList:
    newList.append(data)

oldList.remove('탕수육')
print(oldList)
print(newList)



