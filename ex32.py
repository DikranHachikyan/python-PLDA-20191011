#!/home/wizard/anaconda3/bin/python

def get_squares(n):
    return [ v ** 2 for v in range(n+1)]

def gen_squares(n):
    for v in range(n+1):
        yield v ** 2

def gen_letters(txt):
    for t in txt:
        yield t

if __name__ == '__main__':
    
    ltrs = gen_letters('Hello Python')

    for lt in ltrs:
        print(f'{lt}')    