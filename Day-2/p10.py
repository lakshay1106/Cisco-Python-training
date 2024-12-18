def display(prodID, prodName, pcost):
    print(pid,pname,pcost)

display()
display('p101','prodA')
display('p101','prodA',1000)

def display(*args):
    if(args):
        for v in args:
            print(v)
    else:
        print("empty args")

display()
display('p101','prodA',1000)

def display(**kwargs):
    if(kwargs):
        for var in kwargs:
            print(var,kwargs[var])

    else:
        print("empty args")

display(pid='p101',pname='prodA', pcost=1000)
