import re
txt = '[0-9]{4}/(0?[1-9])/[0-9]{2}'
x=re.match(txt, '1401/02/18')
print(x)