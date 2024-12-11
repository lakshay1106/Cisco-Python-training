pin = 1234
i=0
while(i<3):
    inp = input("Enter the pin: ")
    i = i + 1
    if(int(inp) == pin):
                print(f'Success Pin is matched - {i}')
                break #exit from loop

if(int(inp) != pin):
    print(f'Sorry your pin is blocked')
                
