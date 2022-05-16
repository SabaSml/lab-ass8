import re
txt = 'a*bb(b)*$'
x=re.match(txt, 'abbb')
print(x)