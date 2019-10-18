#!/home/wizard/anaconda3/bin/python
# 1. декларация
val = 100 # глобална променлива

def sum_numbers(a, b, *args):
    # print(type(args))
    # print(args)
    c = a + b
    for v in args:
        c += v
    return c

if __name__ == '__main__':
    # 2. извикване
    x,y = 8,9
    result = sum_numbers(x,y)
    print(f'{x} + {y} = {result}')

    t = [2,3,4,5,6]
    result = sum_numbers(4,7, *t)
    print(f'{4} + {7} + ' + ' + '.join(map(str,t))+ f'= {result}')
    
    result = sum_numbers(4,7, 5, 7, 8, 9)
    print(f'{4} + {7} + ...= {result}')

