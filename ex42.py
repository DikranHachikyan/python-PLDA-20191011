#!/home/wizard/anaconda3/bin/python

def sortKey2(el):
    return el[1]

if __name__ == '__main__':
    lexp = lambda a: a ** 3 if a % 2 else a ** 2

    print(f'1:{lexp(4)}')   
    print(f'2:{lexp(5)}')

    items = [('A',5,7),('Z',2,6),('B',4,6),('D',2,5)]

    # items.sort()
    # print(f'sorted items:{items}')  
    
    # items.sort(key=lambda el: el[1])
    # # items.sort(key=sortKey2)
    # print(f'sorted items:{items}')  
    
    items.sort(key=lambda el: (el[1],el[0]) )
    print(f'sorted items:{items}') 

    nums = [1,2,3,4,5]

    for v in map( lambda a: a + a , nums):
        print(f'v={v}')