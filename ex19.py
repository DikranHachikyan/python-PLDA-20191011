#!/home/wizard/anaconda3/bin/python
# 1. декларация
val = 100 # глобална променлива

def sum_numbers(a,b):
    c = a + b #c - локална променлива
    return c

if __name__ == '__main__':
    # 2. извикване
    x,y = 8,9
    result = sum_numbers(x,y)
    print(f'{x} + {y} = {result}')

    result = sum_numbers(4,7)
    print(f'{4} + {7} = {result}')
