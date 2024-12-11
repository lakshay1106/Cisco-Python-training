#Task1
'''app_name = input("Enter the name of app: ")
port_no = input("Enter the port no: ")


if app_name == "flask" or app_name == "fastapi":
    print(f'app name is :{app_name} running port number is:{port_no}')
else:
    print(f'app name is not matched')
    '''

#Task2

shell_name = input("enter the name of shell: ")
if(shell_name=='bash'):
    fname = 'bashrc'
elif(shell_name =='ksh'):
        fname = 'kshrc'
elif(shell_name == 'csh'):
    fname = 'cshrc'

else:
    shell_name = 'nologin'
    fname = '/etc/profile'

print(f'shell name is: {shell_name} and profile name is: {fname}')
