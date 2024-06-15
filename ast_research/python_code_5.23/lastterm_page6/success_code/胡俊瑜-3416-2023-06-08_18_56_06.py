CurStr = input()

if CurStr[0:3] in "RMB":

    U= (eval(CurStr[3:]))/6.78

    print("USD%.2f"%(U))

elif CurStr[0:3] in "USD":

    R= (eval(CurStr[3:]))*6.78

    print("RMB%.2f"%(R))
elif CurStr[0:1] in "&":

    u= (eval(CurStr[1:]))/6.78

    print("$%.2f"%(u))

elif CurStr[0:1] in "$":

    r= (eval(CurStr[1:]))*6.78

    print("&%.2f"%(r))
else :
    print("Error")



