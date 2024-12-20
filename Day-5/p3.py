import sqlite3

try:
    con = sqlite3.connect('emp.db')

except Exception as eobj:
    print('Exception:',eobj)
finally:
    sth = con.cursor()
    s = 'create table emp_table(eid INT, ename TEXT, edept TEXT, ecity TEXT, ecost INT)'
    sth.execute(s)

with open('emp.csv', 'r') as fobj:
    for var in fobj:
        var = var.strip()
        L = var.split(",")
        sth.execute("insert into emp_table values(?,?,?,?,?)",(L[0],L[1],L[2],L[3],L[4]))

sth.execute("select * from emp_table where ecost > 3000")
for var in sth:
    print(var)
    eid,ename,edept,ecity,ecost = var
    with open("emp.log","a") as wobj:
        wobj.write(f'{eid}\t{ename}\t{edept}\t{ecity}\t{ecost}\n')
