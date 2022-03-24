
from math import sqrt


"""класс"""
class Point:
    """конструктор"""
    def __init__(self,x,y):
        self.x = x
        self.y = y

    """метод"""
    def distance(self, p2):
        dx = p2.x - self.x
        dy = p2.y - self.y
        return sqrt(dx*dx + dy*dy)

    """переопреледили операцию сравнения"""
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    """переопреледили операцию сортировки"""
    def __lt__(self, other):
        return self.y < other.y

    """переопреледили операцию вывода на консоль"""
    def __repr__(self):
        return "Point(%s,%s)" %(self.x, self.y)