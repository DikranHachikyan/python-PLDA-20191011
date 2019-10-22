#!/home/wizard/anaconda3/bin/python

# import time
from time import time,sleep
from functools import wraps

def measure(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        t = time()
        func(*args,**kwargs)
        print(f'{func.__name__} : {time() - t:.8f}')
        print(f'{func.__doc__}')
    return wrapper

@measure
def foo(sleep_time=0.3):
    '''Function foo sleeps sleep_time seconds'''
    sleep(sleep_time)


@measure
def cube(n):
    '''return list of cubes'''
    for v in range(n+1):
        print(v)


cube(10)
