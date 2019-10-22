#!/home/wizard/anaconda3/bin/python

# import time
from time import time,sleep

def foo(sleep_time=0.3):
    '''Function foo sleeps sleep_time seconds'''
    sleep(sleep_time)


def measure(func):
    def wrapper(*args,**kwargs):
        t = time()
        func(*args,**kwargs)
        print(f'{func.__name__} : {time() - t:.4f}')
        print(f'{func.__doc__}')
    return wrapper


f = measure(foo)

f(0.5)

print(f'{f.__name__}:{f.__doc__}')





