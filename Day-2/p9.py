import pprint
file = open('prod_info.log', 'a')

prod_info = {'prodID':[], 'prodName':[], 'salesCount':[]}

i=0
while(i<3):
    pr_id = input('Enter product id: ')
    pr_name = input('Enter Product name: ')
    pr_sales = input('Enter Product sales count: ')

    file.write(pr_id+","+pr_name+","+pr_sales+"\n")
    i+=1
