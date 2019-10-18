#!/home/wizard/anaconda3/bin/python
# 1. декларация

def show(title,*args,**kwargs):
    print(f'Positional: title={title}')

    if args:
        print('List of args:')
    for v in args:
        print(f'arg:{v}')

    if kwargs:
        print('Keyword params:')
    if 'ip' in kwargs:
        print(f'gateway:{kwargs["ip"]}')
    
    if 'path' in kwargs:
        print(f'path:{kwargs["path"]}')

if __name__ == '__main__':
    # 2. извикване
    show('Text Editor')

    show('Text Editor',11,22,33)

    # Ok!
    # show('Text Editor',22,44,66,ip='192.168.1.1', path='/usr/local')
    
    # Ok!
    # show('Text Editor',ip='192.168.1.1', path='/usr/local')

    config = {
        'ip':'192.168.1.1'
        , 'path':'/usr/local'
    }

    show('Text Editor', **config)