#!/home/wizard/anaconda3/bin/python

class Point():
    # Конструктор на класа
    def __init__(self, x=0, y=0):
        print('Constructor Point')
        self.__x = x # променлива на обекта
        # x = 10    # локална променлива
        self.__y = y

    # Методи на класа
    def moveTo(self, dx,dy):
        self.__x += dx
        self.__y += dy

    def show(self):
        print(f'Draw Point:({self.__x},{self.__y})')

if __name__ == '__main__':
    # Point - клас; типа, който сме създали
    # p1 - обект; екземпляр от типа Point
    print('begin') 
    p1 = Point()
    print('end') 

    # p1.__x = 100
    p1.show()
    p1.moveTo(-30,20)
    p1.show()


    p2 = Point(120,300)

    p2.show()