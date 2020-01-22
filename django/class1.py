# class 클래스명:
#      함수
#      함수

# class User:
#     def __init__(self, name, age):
#         print('생성자 호출')
#         self.name = name
#         self.age = age
#     #def __init__(self, name):
#     #    self.name = name
#     def getInfo(self):
#         print(self.name+','+str(self.age))
#
#
# u1 = User('강가딘',6)
# print(u1.name)
# u1.getInfo()
# # print(u1.getInfo()) => getInfo()에 리턴 값이 없어서 print()시 None
# u2 = User('이몽룡', 16)
# print(u2.name)
# u3 = User('성춘향')
# print(u3.name)
#-----------------
# class Car:
#     def __init__(self,color,tp):
#         self.type = tp
#         self.color = color
#     def show(self):
#         return 'Car의 show메서드 호출'
#
# class BmwCar(Car): # Car를 상속받은 BmwCar
#     def __init__(self,name, color, tp):
#         super().__init__(color, tp)
#         self.name = name
#     def showname(self):
#         return '내차는 '+ self.name
#
# class BenzCar(Car):
#     def __init__(self, name, color, tp):
#         super().__init__(color, tp)
#         self.name = name
#     def showname(self):
#         return '내차는 '+self.name
#     def show(self):
#         return 'BenzCar의 show메서드'
#
#
# c1 = BmwCar('100', '흰색', '세단')
# print(c1.showname())
# print(c1.show())
#
# c2 = BenzCar('200', '비둘기색', 'suv')
# print(c2.showname())
# print(c2.show())
#
# print(BmwCar.mro()) # mro()는 상속관계를 나타낸다.
# print(BenzCar.mro())
#-------------------------
# Object를 상속받은 클래스
class X(object):
    pass
class Y():
    pass
class Z:
    pass

class A(X,Y):
    pass

class B(Y,Z):
    pass

class C(A,B):
    pass

print(C.mro())