class Point():
    count = 0
    # Конструктор на класа
    def __init__(self, x=0, y=0):
        # Данни на обекта
        self._x = x
        self._y = y
        Point.count += 1

    # Методи на класа
    def moveTo(self, dx,dy):
        self._x += dx
        self._y += dy

    def show(self):
        print(f'Draw Point:({self._x},{self._y}) Count:{Point.count}')

    # Специални методи

    def __add__(self,other):
        """ p = p1 + p2 """
        if not isinstance(other,Point):
            return NotImplemented
        return Point( self._x + other._x, self._y + other._y)
    
    def __iadd__(self,other):
        """ p1 = p1 + p2 in-place addition"""
        # print('in-place addition')
        if not isinstance(other,Point):
            return NotImplemented
        self._x += other._x
        self._y += other._y

        return self

    def __str__(self):
        """str(obj) => string"""
        return f'({self._x},{self._y})'

    def __eq__(self,other):
        """ if p1 == p2: ... """
        if not isinstance(other,Point):
            return NotImplemented
        #return abs(self._x - other._x)< 10 ...
        return self._x == other._x and self._y == other._y
    
    def __del__(self):
        """finalize()"""
        Point.count -= 1

    #методи за достъп до данните

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self,x):
        assert type(x) is int and x >= 0 , 'x must be positive number'
        self._x = x

    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self,y):
        assert type(y) is int and y >= 0 , 'y must be positive number'
        self._y = y