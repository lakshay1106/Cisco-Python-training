import time

file = open("pin_history.log","a")

pin = 1234
count = 0
while(count<3):
    p = input('Enter a pin number: ')
    count = count+1
    if(int(p) == pin):
        file.write(f'Success - pin is matched - {count} ')
        file.write(f'Pin Entry time is:{time.ctime() } \n')
        print(f'Success - Pin is matched - {count}')
        break
    else:
        file.write(f'failed - user input pin:{p}')
        file.write(f'Pin Entry time is:{time.ctime() } \n')

if(int(p) != pin):
    file.write('Blocked-Your max input limit crossed\n')
    print('Sorry your pin is blocked')


file.close()
