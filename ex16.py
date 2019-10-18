#!/home/wizard/anaconda3/bin/python

if __name__ == '__main__':
    user = {
        'id':11
        , 'name':'anna'
        , 'mail':'anna@no.com'
        , 'age':30
    }
    
    for data in user.items():
        key,value = data
        print(f'data = {data}, key={key}, value={value}')