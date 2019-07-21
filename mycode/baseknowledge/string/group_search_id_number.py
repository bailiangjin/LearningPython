import re

s = '11022319901220123X'
res = re.search('(?P<province>\d{3})(?P<city>\d{3})(?P<born_year>\d{4})(?P<born_day>\d{4})(?P<born_number>(\d{3}[0-9Xx]))',s)
print(res.groupdict())