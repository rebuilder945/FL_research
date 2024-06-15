MoneY=input()
if MoneY[0] in ["&"]:
    $=(eval(MoneY[1:])*6.78)
    print("%.2f$"%($))
elif MoneY[0] in ["$"]:
    &=(eval(MoneY[1:])/6.78)
    print("%.2f&"%(&))
elif MoneY[0:3] in ["RMB"]:
    USD=(eval(MoneY[3:])*6.78)
    print("%.2fUSD"%(USD))
elif MoneY[0:3] in ["USD"]:
    RMB=(eval(MoneY[3;])/6.78)
    print("%.2fRMB"%(RMB))
else:
    print("Error")

