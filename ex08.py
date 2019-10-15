#!/home/wizard/anaconda3/bin/python

if __name__ == '__main__':
    # 1+2+3+...+99+100 = 5050

    i = 1000
    nSum = 0

    while i <= 100:
        nSum += i # nSum = nSum + i
        i += 1    # i = i + 1
    else:
        print('--- else ---')

    print(f'1+2+3+...+99+100={nSum}')