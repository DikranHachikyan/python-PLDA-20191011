#!/home/wizard/anaconda3/bin/python
# 1. декларация
val = 100 # глобална променлива

def sum_numbers(a, b, d=0):
    c = a + b + d
    return c

if __name__ == '__main__':
    # 2. извикване
    x,y = 8,9
    result = sum_numbers(x,y)
    print(f'{x} + {y} = {result}')

    result = sum_numbers(4,7,8)
    print(f'{4} + {7} + {8}= {result}')

