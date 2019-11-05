#!/home/wizard/anaconda3/bin/python
import re

if __name__ == '__main__':
   names = None
   
   pattern = re.compile(r'([A-Z][a-z]+)\s+\w*\s*([A-Z][a-z]+)')
   while names == None:
        names = input('FirstName and LastName:')
        m = pattern.match(names)
        if m:
           print(f'{names}: Group:{m.group()} First Name:{m.group(1)} Last Name:{m.group(2)}')
        else:
            names = None