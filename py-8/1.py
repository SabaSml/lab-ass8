import re
txt = '^(\+)[1-9][0-9\-]{7,32}$'
x= re.match(txt, "+98-915-345-6789")
print(x)