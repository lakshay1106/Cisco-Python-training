prod_list = ['p101,prodA,1000','p102,prodB,2000','p103,prodC,3000']

file = open('prod.csv','w')
for var in prod_list:
    print(var,type(var))

for var in prod_list:
    file.write(var+"\n")

file.close()
