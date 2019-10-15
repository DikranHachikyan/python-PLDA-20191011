#!/home/wizard/anaconda3/bin/python

def show():
    print('Hello Pyton')

if __name__ == '__main__':
    x = int(input('x = '))

    if x > 0 :
        print(f'x is positive number ({x})')
    else:
        print(f'x is negative or zero ({x})')
    
    show()