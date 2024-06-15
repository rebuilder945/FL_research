Money=input()
if Money[0] in ["$"]:
    D=eval(Money[1:])*6.78
    print("&%.2f"%(D))
elif Money[0:3] in ["USD"]:
    C=eval(Money[3:])*6.78
    print("RMB%.2f"%(C))
elif Money[0] in ["&"]:
    B=eval(Money[1:])/6.78
    print("$%.2f"%(B))
elif Money[0:3] in ["RMB"]:
    A=eval(Money[3:])/6.78
    print("USD%.2f"%(A))
else:
    print('Error')

