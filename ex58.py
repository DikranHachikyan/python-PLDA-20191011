#!/home/wizard/anaconda3/bin/python
import re

if __name__ == '__main__':
   names = None
   
   pattern = re.compile(r'(?P<first>[A-Z][a-z]+)\s+\w*\s*(?P<last>[A-Z][a-z]+)')
   while names == None:
        names = input('FirstName and LastName:')
        m = pattern.match(names)
        if m:
           print(f'{names}: Group:{m.group()}')
           print(f"First Name:{m.group('first')} Last Name:{m.group('last')}")
        else:
            names = None