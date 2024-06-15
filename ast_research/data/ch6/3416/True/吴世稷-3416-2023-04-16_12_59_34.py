qian=input()
if qian[0]in["$"]:
    R = eval(qian[1:])*6.78
    print("&%.2f"%(R))
elif qian[0:3]in["USD"]:
    R = eval(qian[3:])*6.78
    print("RMB%.2f"%(R))
elif qian[0]in["&"]:
    U = eval(qian[1:])/6.78
    print("$%.2f"%(U))
elif qian[0:3]in["RMB"]:
    U = eval(qian[3:])/6.78
    print("USD%.2f"%(U))
else:
    print("Error")


