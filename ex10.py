#!/home/wizard/anaconda3/bin/python

if __name__ == '__main__':
    # 1+2+...+99+100 = 2550

    i = 1
    nSum = 0

    while i <= 100:
        print(f'i={i}')
        if i == 5: break 
        nSum += i 
        i += 1    
    else:
        print('--- else ---')

    print(f'1+2+3+...+99+100={nSum}')