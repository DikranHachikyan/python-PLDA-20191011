#!/home/wizard/anaconda3/bin/python
# 1. декларация

def show(title,*,kw1='a',kw2='b',**kwargs):
    print(f'Positional: title={title}')
    
    print(f'Keyword only:kw1={kw1},kw2={kw2}')

    if kwargs:
        print('Keyword params:')
    
    k_params = {
        'ip': kwargs.get('ip','127.0.0.1')
        , 'path': kwargs.get('path','/tmp')
    }
    
    print(f'k params:{k_params}')

if __name__ == '__main__':
    # 2. извикване
    
    config = {
        'ip':'192.168.1.1'
        , 'path':'/usr/local'
    }
    
    show('Text Editor',kw2='Python', **config)
    show('Text Editor', path='/home')