Money = input()
if Money[0] =='$':
    C = (eval(Money[1:])*6.78
    print("&"+"%.2f"%(C))
elif Money[0:3]=="USD":
    a=(eval(Money[3:]))*6.78
    print("RMB"+"%.2f"%a)
elif Money[0]=="&":
    b=(eval(Money[1:]))/6.78
    print('$'+"%.2f'%b)
elif Money[0:3]=="RMB"
    d=(eval(Money[3:]))/6.78
    print("USD"+"%.2f"%d)
else:
    print("Error")
