#!/home/wizard/anaconda3/bin/python
# 1. декларация

def sum_numbers(a,b,c=0):
    d = a + b + c
    return d

if __name__ == '__main__':
    # 2. извикване
    x,y,z = 5,6,9

    res = sum_numbers(x,y)
    print(f'{x} + {y} = {res}')
    
    res = sum_numbers(x,y,z)
    print(f'{x} + {y} + {z}= {res}')