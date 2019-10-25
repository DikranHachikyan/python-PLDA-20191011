#!/home/wizard/anaconda3/bin/python

from functools import wraps

def upperCase(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        args = [ v.upper() for v in map(str,args)]
        return func(*args,**kwargs)
    return wrapper

def brackets(left='[',right=']'):
    def decorator(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            args = [f'{left}{v}{right}' for v in args]
            return func(*args,**kwargs)
        return wrapper
    return decorator


@brackets('{','}')
@upperCase
def concat(*args,**kwargs):
    '''Concatenate agrs with sep'''
    sep = kwargs.get('sep',' ; ')
    return sep.join(args)


if __name__ == '__main__':
    countries = ['bg','us','de','uk','fr']

    print(concat(*countries,sep=' | '))
    print(concat('anna','maria','markus','john',sep=' $ '))
    print(concat(11,22,33,44,55,sep=' - '))
    print(f'{concat.__name__},{concat.__doc__}')

    print = upperCase(print)
    print('hello python')
