MoneY=input()
if MoneY[0] in ["&"]:
    c=(eval(MoneY[1:])*6.78)
    print("$%.2f"%(c))
elif MoneY[0] in ["$"]:
    c=(eval(MoneY[1:])/6.78)
    print("&%.2f"%(c))
elif MoneY[0:3] in ["RMB"]:
    f=(eval(MoneY[3:])*6.78)
    print("USD%.2f"%(f))
elif MoneY[0:3] in ["USD"]:
    f=(eval(MoneY[3;])/6.78)
    print("RMB%.2f"%(f))
else:
    print("Error")

