products = {}  #empty dictionary

while(True):
    pid = input('Enter a product id: ')
    if pid in products:
        print(f'Product id: {pid} is already exists')
    else:
        pname = input('Enter a product name: ')
        products[pid] = pname   #adding new data to an existing dict


    choice = input('Wish to exit type Yes or press Y: ')
    if(choice == 'Yes' or choice == 'Y'):
        break


print("List of product details:- ")
print("-"*30)

for var in products:
    print(f'{var}\t{products[var]}')
        