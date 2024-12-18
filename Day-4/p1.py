fobj =open('inputFile.csv', 'r')
L = fobj.readlines()
fobj.close()
for var in L:
    if('sales' in var):
        L1 = var.split(',')
        print(f'{L1[1]}\t{L2[2]}')




#list(map(lambda a1:a1.split(',')[1:3],filter(lambda a:'sales' in a,open('emp.csv','r'))))
