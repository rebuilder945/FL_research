n=input()
if n[0] in ["$"]:
    R=(eval(n[0:-1]))*6.78
    print("&%.2f"%R)
if n[0] in ["&"]:
    M=(eval(n[0:-1]))/6.78
    print("$%.2f"%M)
if n[0:3] in ["RMB"]:
    M=(eval(n[2:-1]))*6.78
    print("USD%.2f"%M)
if n[0:3] in ["USD"]:
    R=(eval(n[2:-1]))*6.78
    print("RMB%.2f"%R)
else:
    print("Error")


