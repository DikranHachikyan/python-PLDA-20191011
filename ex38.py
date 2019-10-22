#!/home/wizard/anaconda3/bin/python

# import time
from time import time,sleep
from functools import wraps



def measure(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        t = time()
        func(*args,**kwargs)
        print(f'{func.__name__} : {time() - t:.4f}')
        print(f'{func.__doc__}')
    return wrapper

@measure
def foo(sleep_time=0.3):
    '''Function foo sleeps sleep_time seconds'''
    sleep(sleep_time)


foo(0.5)

print(f'{foo.__name__}:{foo.__doc__}')





