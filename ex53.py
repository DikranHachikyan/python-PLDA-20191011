#!/home/wizard/anaconda3/bin/python

class Point():
    count = 0
    # Конструктор на класа
    def __init__(self, x=0, y=0):
        # Данни на обекта
        self.__x = x
        self.__y = y
        Point.count += 1

    # Методи на класа
    def moveTo(self, dx,dy):
        self.__x += dx
        self.__y += dy

    def show(self):
        print(f'Draw Point:({self.__x},{self.__y}) Count:{Point.count}')

    # Специални методи

    def __add__(self,other):
        """ p = p1 + p2 """
        if not isinstance(other,Point):
            return NotImplemented
        return Point( self.__x + other.__x, self.__y + other.__y)
    
    def __iadd__(self,other):
        """ p1 = p1 + p2 in-place addition"""
        # print('in-place addition')
        if not isinstance(other,Point):
            return NotImplemented
        self.__x += other.__x
        self.__y += other.__y

        return self

    def __str__(self):
        """str(obj) => string"""
        return f'({self.__x},{self.__y})'

    def __eq__(self,other):
        """ if p1 == p2: ... """
        if not isinstance(other,Point):
            return NotImplemented
        #return abs(self.__x - other.__x)< 10 ...
        return self.__x == other.__x and self.__y == other.__y
    
    def __del__(self):
        """finalize()"""
        Point.count -= 1

    # 

if __name__ == '__main__':
    p1 = Point(4,5)
    p2 = Point(7,8)

    p1.show()
    del p1
    p2.show()