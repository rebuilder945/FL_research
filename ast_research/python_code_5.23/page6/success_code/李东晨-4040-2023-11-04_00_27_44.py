x=input()
if x[0]=='$':
    y=6.78*eval(x[1:])
    print("&%.2f"%(y))
elif x[0]=='&':
    y=eval(x[1:])/6.78
    print('$%.2f'%(y))
elif x[0]=="R":
    y=eval(x[3:])/6.78
    print('USD%.2f'%(y))
elif x[0]=="U":
    y=eval(x[3:])*6.78
    print("RMB%.2f"%(y))
else:
    print("Error")
