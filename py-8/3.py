import re
txt = 'a*(ba*ba*)*ba*$'
x=re.match(txt, 'babab') 
print(x)