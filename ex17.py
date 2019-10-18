#!/home/wizard/anaconda3/bin/python

if __name__ == '__main__':
    lst = [ x ** 2 for x in range(10)]

    print(lst)

    letters = [v for v in 'hello python']
    print(letters)

    print('#'.join(letters))

    print('|'.join(str(c) for c in lst))
    print('|'.join(map(str,lst)))