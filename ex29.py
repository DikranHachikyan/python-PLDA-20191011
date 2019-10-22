#!/home/wizard/anaconda3/bin/python
# 1. декларация

def show(a = [], b = {}):
    print(f'a = {a}')
    print(f'b = {b}')
    print('-' * 12)
    a.append(len(a))
    b[len(a)] = len(a)

if __name__ == '__main__':
    # 2. извикване
    show()
    show([5,6,7],{'B':100})
    show()
    show([11,67],{'D':40})
    show()