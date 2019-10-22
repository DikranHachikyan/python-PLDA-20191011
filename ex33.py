#!/home/wizard/anaconda3/bin/python

def gen_squares(start,end):
    yield from ( v ** 2 for v in range(start,end))

if __name__ == '__main__':
    
    squares = ( v ** 2 for v in range(11))

    print(next(squares))
    print(next(squares))
    print(next(squares))
    print(next(squares))

    ls = list(gen_squares(5,10))
    print(ls)