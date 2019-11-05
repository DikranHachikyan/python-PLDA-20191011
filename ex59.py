#!/home/wizard/anaconda3/bin/python
import re

if __name__ == '__main__':
   txt = 'hello python, java and javascript, c+++'
   pattern = re.compile(r'(\w+\+{,2})')
   
   for m in pattern.finditer(txt):
       print(f'start:{m.start()} end:{m.end()} span:{m.span()}')
       print(f'group:{m.group(1)}')