file = open('emp.csv', 'r')
fobj = file.readlines()
file.close()
print(fobj)

print("Emp Name    Emp Department")

for i in fobj:
    n = i.split(",")
    print(n[1],"\t\t", n[2])

