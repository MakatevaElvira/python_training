import pickle

from point import Point

a = Point(0,0)
b = Point( 3,4)
print(a.distance(b))
print(a==b)
print(a==Point(0,0))

l1 = [Point(3, 1), Point (0, 0), Point(1, 2)]
l2 = sorted(l1)

def x(p):
    return p.x

def y(p):
    return p.y
"""lambda"""
l2 = sorted(l1,key=x)
l3 = sorted(l1,key= lambda p: p.x)
l5 = sorted(l1,key= lambda p: p.distance(Point(0,0)))

print(l1)
print(l5)

l11 = []

for i in range(-5, 6):
    l11.append(Point(i,i*i))

print(l11)

for el in l11:
    el.y = - el.y
#print(el)
print(l11)

"""cycle"""
l12 = []
for el in l11:
    l12.append(Point(el.x,-el.y))

print(l12)

"""analog for l12  = list comprehension"""
l13 = [Point(el.x,-el.y) for el in l11]
l130 = list(map(lambda p:Point(p.x,-p.y), l11))
print(l13)
print(l130)

"""range = диапазон"""
l110 = [Point(i,i*i) for i in range(-5, 6)]

"""элементы функционального программирования, когда функция является обьектом 
и ее можно передать в качестве параметра"""

"""list для превращения в список функции мар"""
l101 = list(map(lambda i: Point(i,i*i), range(-5, 6)))
"""фильтрация  списка"""
l1010 = list(filter(lambda p: p.x %2 == 0, l101))
print(l110)
print(l101)
print(l1010)
