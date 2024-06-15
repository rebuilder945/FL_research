money=input("")
money=list(money)


if money[0] in ["&"]:

    C = eval(''.join(money[1:]))/6.78

    print("$%.2f"%(C))
elif money[0] in ["$"]:

    F = 6.78*eval("".join(money[1:]))

    print("&%.2f"%(F))
elif ''.join(money[0:3]) in ["RMB"]:

    B = eval("".join(money[3:]))/6.78

    print("USD%.2f"%(B))
elif ''.join(money[0:3]) in ["USD"]:

    E = 6.78*eval("".join(money[3:]))

    print("RMB%.2f"%(E))





else:

    print("Error")
