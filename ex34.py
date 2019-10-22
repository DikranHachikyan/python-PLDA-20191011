#!/home/wizard/anaconda3/bin/python

# import time
from time import time

if __name__ == '__main__':
    values = []
    N = 5000

    t = time()
    for v in range(1,N):
        for s in range(v,N):
            values.append(divmod(v,s))
    print(f'for loop:{time()-t:.4f}')

    t = time()
    values2 = [ divmod(v,s) for v in range(1,N) for s in range(v,N)]
    print(f'for expression:{time()-t:.4f}')

    t = time()
    values2 = list( (divmod(v,s) for v in range(1,N) for s in range(v,N)) )
    print(f'generator:{time()-t:.4f}')