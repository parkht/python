import matplotlib as mpl
import matplotlib.pylab as plt
import matplotlib.font_manager as fm
# 그래프 세팅
# 제목
plt.title("Line plot")
font_name = fm.FontProperties(fname='C:\Windows\Fonts\H2GPRM.TTF').get_name()
print(font_name)
mpl.rc('font', family=font_name)
# 데이터 세팅
# x 좌표는 인덱스 값을 사용한다.
# plt.plot([1,4.5,2.3,6,3,8,5,9,10])
# x 좌표 값을 설정 plt.plot([x좌표의 값],[y좌표의 값],'라인속성',값의 이름)
# rs-- : r(red,색깔), s(square), o() --(점선) -(실선)
# c:선색, lw:선의 굵기, ls:선 스타일, marker:데이터 위치의 마커(마커의 모양), ms(marker size):마커크기
# mec:마커 테두리 색, mew: 마커 테두리 굵기, mfc : 마커 내부 색
plt.plot([2012,2013,2014,2015,2016,2017,2018,2019,2020],[1,3,2.3,6,4,8,5,9,10],'rs--',label='a')
plt.plot([2012,2013,2014,2015,2016,2017,2018,2019,2020],[10,6,9,5,8,4,7,3,1],'bs',label='b')
plt.plot([2012,2013,2014,2015,2016,2017,2018,2019,2020],[6,7,5,6,7,6,7,5,6],'go-',label='c',mfc='c')
# x, y 축의 라벨세팅
plt.xlabel('년도', fontdict={'family':font_name}, fontsize=16)
plt.ylabel('값', family=font_name, fontsize=12)
plt.legend(loc='best')

plt.show()


