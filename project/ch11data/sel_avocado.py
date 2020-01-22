from bs4 import BeautifulSoup
fp = open("fruit_vegetables.html",encoding='utf-8')
soup = BeautifulSoup(fp,'html.parser')

# CSS 선택자로 추출하기
# print(soup)
# print(soup.select_one('li:nth-of-type(5)'))=> 모든 li에서 찾는 것이 아니라 그룹들마다 li를 찾고 그룹별로 li순서를 정한다.
# 그룹이 바뀌면 순서는 다시 1로 시작하기 때문에 'a'그룹의 첫번째 'li'와 'b' 그룹의 첫번째 'li'가 중복이 되서
# 'a'그룹의 첫번째 'li'만 출력이 된다.

print(soup.select_one('#ve-list > li:nth-of-type(4)').string)
print(soup.select("#ve-list > li[data-lo='us']")[1].string)
print(soup.select("#ve-list > li.black")[1].string)

# find 메서드로 추출하기
cond = {'data-lo':'us', 'class':'black'}
print(soup.find('li', cond).string)

# find 메서드를 연속적으로 사용하기
print(soup.find(id='ve-list').find('li',cond).string)
