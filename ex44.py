#!/home/wizard/anaconda3/bin/python

def foo():
    keys = {
        '+':'sum numbers'
    }
    try:
        num1 = float(input('Enter a number:'))
        op = input('Action (+):')
        print(f'num1 = {num1}')
        print(f'{op} {keys[op]}')
        return
    except ValueError as e:
        print(f'not a number:{e}')
    except KeyError as e:
        print(f'invalid key:{e}')
    except:
        print('unknown exception')
    else:
        print('--- else --- (when no exception)')
    finally:
        print('--- finally --- (always - clean up)')

if __name__ == '__main__':
    foo()