#!/home/wizard/anaconda3/bin/python

class NegativeValueError(Exception):
    pass

def sumNumbers(a,b):
    if a < 0 or b < 0:
        raise NegativeValueError(f'negative number:a={a} b={b}')
    c = a + b
    return c    

if __name__ == '__main__':
    try:
        print(f'res = {sumNumbers(5,6)}')
        print(f'res = {sumNumbers(-5,5)}')
        print(f'res = {sumNumbers(7,9)}')
    except NegativeValueError as e:
        print(f'Error:{e}')