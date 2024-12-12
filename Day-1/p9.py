DBs = ['oracle', 'sql', 'mysql', 'plsql']
v = input('Enter a db name: ')
if(v in DBs):
    print(f'Yes input db: {v} is exists - index number is: {DBs.index(v)}')
else:
    print(f'Input db:{v} is not exists - will add to DBs')
    DBs.append(v)

print(f'All Dbs of list')
for i in DBs:
    print(f'{i}')
    
