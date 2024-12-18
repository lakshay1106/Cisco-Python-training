import re
used_size = ['120G','100GB','200g','300','150Gb']
total = 0;
for var in used_size:
    s = re.sub('[A-za-z]','',var)
    total = total+int(s)

else:
    print(f'Sum of used_size: {total} GB')
