#!/home/wizard/anaconda3/bin/python

if __name__ == '__main__':
    # 2+4+...+98+100 = 2550

    i = 1
    nSum = 0

    while i <= 3:
        i += 1    
        if ( i % 2) != 0: continue 
        nSum += i 
    else:
        print('--- else ---')

    print(f'1+2+3+...+99+100={nSum}')