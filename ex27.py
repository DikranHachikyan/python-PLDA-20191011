#!/home/wizard/anaconda3/bin/python
# 1. декларация

def sum_numbers(n):
    print(f'n={n}')
    if n > 0:
        return n + sum_numbers( n - 1) # рекурсивно извикване
    return 0

if __name__ == '__main__':
    # 2. извикване
    x = 6

    res = sum_numbers(x)
    print('sum ' + '+'.join(map(str,range(x+1))) + f'={res}')