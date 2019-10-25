#!/home/wizard/anaconda3/bin/python

def sumNumbers(a,b):
    c = 0
    try:
        if a < 0 or b < 0:
            raise ValueError(f'negative number:a={a} b={b}')
        c = a + b
    except ValueError:# as e:
        pass
        # print(f'Error:{e}')
        # return None

    return c    

if __name__ == '__main__':
    print(f'res = {sumNumbers(5,6)}')
    print(f'res = {sumNumbers(-5,5)}')
    print(f'res = {sumNumbers(7,9)}')