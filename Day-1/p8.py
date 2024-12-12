hosts = []
print(f'Total no.of hosts: {len(hosts)}')

count = 0
while(count<5):
    h = input("Enter a hostname: ")
    hosts.append(h)
    count=count+1

print('\nlist of host: ')

for var in hosts:
    print(var)

else:
    print(f'Total no. of hosts: {len(hosts)}')
