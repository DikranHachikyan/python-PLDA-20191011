#!/home/wizard/anaconda3/bin/python

class Point():
    # Данни на класа
    label = 'Start'
    # Конструктор на класа
    def __init__(self, x=0, y=0):
        print('Constructor Point')
        # Данни на обекта
        self.__x = x
        self.__y = y

    # Методи на класа
    def moveTo(self, dx,dy):
        self.__x += dx
        self.__y += dy

    def show(self):
        print(f'Draw Point:({self.__x},{self.__y})')

if __name__ == '__main__':
    p1 = Point(4,5)

    p1.show()
    print(f'p1 label:{p1.label}')
    Point.label = 'begin' # label е променлива на класа т.е. достъпна е без да 
                          # създаваме обект

    p2 = Point(7,8)
    p2.show()
    print(f'p2 label:{p2.label}')