#!/home/wizard/anaconda3/bin/python

if __name__ == '__main__':
    x = int(input('x = '))

#Python:  true_expr if condition else false_expr
#C,C++,Java,JavaScript,...  (condition)? true_expr:false_expr 
    m = x if x > 0 else 100

    print(f'm = {m}')
#   if x > 0:
#      m = x
#   else:
#      m = 100 