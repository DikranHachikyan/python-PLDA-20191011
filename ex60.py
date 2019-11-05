#!/home/wizard/anaconda3/bin/python
import re

if __name__ == '__main__':
    match = re.search(r'\d+\D\d+\D\d+',r' Maria: 986-56-93')
#    match = re.match(r'\s\w+\s\d+\D\d+\D\d+',r' Maria 986-56-93')
    print(match.group() if match else 'pattern not found')

    match = re.fullmatch(r'[A-Z]\d{2}\D\d{2}',r'a12-67',re.I)
    print( match.group() if match else 'pattern not found')

    txt = r'For a complete: guide on regular expressions and the python re module, please visit the official documentation.' 
    result = re.split(r'[\s:,\.]',txt)
    print(result)

    txt = r'For a complete: guide 05.11.2019 06.11.2019'
    result = re.findall(r'\d{2}\.\d{2}\.\d{4}', txt)
    print(result)

    result = re.sub(r'\d{2}\.\d{2}\.\d{4}',r'xx.yy.zzzz',txt)
    print(result)