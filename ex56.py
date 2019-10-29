#!/home/wizard/anaconda3/bin/python
import re

if __name__ == '__main__':
   names = None
   
   pattern = re.compile(r'[A-Z][a-z]+\s+[A-Z][a-z]+')
   while names == None:
        names = input('FirstName and LastName:')
        m = pattern.match(names)
        if m:
           print(f'{names}: Start:{m.start()} End:{m.end()} Span:{m.span()}')
        else:
            names = None