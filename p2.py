emp_name = input('Enter the name of employee: ')
emp_id = input(f'Enter  {emp_name} emp id: ')
emp_dept = input(f'Enter {emp_name} working dept: ')
emp_cost = input(f'Enter {emp_name} basic pay: ')

tax = float(emp_cost) * 0.12
total = tax + float(emp_cost)

print(f'''About{emp_name} details:-
----------------------------
Emp name: {emp_name} Emp_id:{emp_id}

{emp_name} working dept is:{emp_dept}
==============================
{emp_name} Cost is : {emp_cost}
==================================
Tax amount : {tax}
Gross Pay(including tax) : {total}
-------------------------------------''')
               
