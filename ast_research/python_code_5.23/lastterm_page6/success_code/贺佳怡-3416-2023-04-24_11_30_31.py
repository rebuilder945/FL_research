n=input()
if n[0] in ["&"] or n[0] in ["R"]:
    if n[0]=="&":
        m=(eval(n[1:]))/6.78
        m="%.2f"%m
        f="$"
        f+=m
        print(f)
    elif n[0]=="R":
        m=(eval(n[3:]))/6.78
        m="%.2f"%m
        f="USD"
        f+=m
        print(f)
elif n[0] in ["$"] or n[0] in ["U"]:
    if n[0]=="$":
        m=(eval(n[1:]))*6.78
        m="%.2f"%m
        f="&"
        f+=m
        print(f)
    elif n[0]=="U":
        m=(eval(n[3:]))*6.78
        m="%.2f"%m
        f="RMB"
        f+=m    
        print(f)
else:
    print("Error")
