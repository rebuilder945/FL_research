Money = input()

if Money[0] in ['$']:
    C = (eval(Money[1:])*6.78
    print("&%.2f"%(C))
elif Money[0] in ["U"]:
    a=(eval(Money[3:]))*6.78
    print("RMB%.2f"%a)
elif Money[0] in ["&"]:
    b=(eval(Money[1:]))/6.78
    print('$%.2f'%b)
elif Money[0] in ["R"]:
    d=(eval(Money[3:]))/6.78
    print("USD%.2f"%d)
else:
    print("Error")
