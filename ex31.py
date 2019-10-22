#!/home/wizard/anaconda3/bin/python

def get_squares(n):
    return [ v ** 2 for v in range(n+1)]

def gen_squares(n):
    for v in range(n+1):
        yield v ** 2

if __name__ == '__main__':
    
    lst = get_squares(10)
    print(f'squared numbers:{lst}')

    #1. присвояваме ген. на променлива
    sq = gen_squares(10)

    #2. next
    print(f'next number:{next(sq)}')
    print(f'next number:{next(sq)}')
    print(f'next number:{next(sq)}')
    print(f'next number:{next(sq)}')

    print(type(gen_squares))
    print(type(sq))

    sq = gen_squares(4)

    for v in sq:
        print(f'{v}')
    
    print('-' * 12 )

    sq = gen_squares(4)
    print(next(sq))
    print(next(sq))
    print(next(sq))
    print(next(sq))
    print(next(sq))
    # after last 
    print(next(sq))