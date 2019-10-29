#!/home/wizard/anaconda3/bin/python

# 1.
# import draw
# или
# import draw.point

# 2.
#from draw.point import Point

# 3.
from draw import Point2D as Point
# import draw

if __name__ == '__main__':
    # 1
    # p1 = draw.point.Point(10,29)
    # p1.show()

    # 2
    # p1 = Point(10,20)
    # p1.show() 

    # 3. 
    #p1 = draw.Point(4,5)
    p1 = Point(4,5)
    p1.show() 