#!/home/wizard/anaconda3/bin/python

class Point():
    # Конструктор на класа
    def __init__(self):
        print('Constructor Point')
        self.x = 10 # променлива на обекта
        # x = 10    # локална променлива
        self.y = 5

if __name__ == '__main__':
    # Point - клас; типа, който сме създали
    # p1 - обект; екземпляр от типа Point
    print('begin') 
    p1 = Point()
    print('end') 

    print(f'p1:({p1.x}, {p1.y})')