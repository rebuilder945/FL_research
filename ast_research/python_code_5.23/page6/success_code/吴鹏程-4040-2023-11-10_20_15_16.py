money=input()
if money[0] in ["U"]:
    meijing=(eval(money[3:]))*6.78
    print("RMB%.2f"%(meijing))
elif money[0] in ["$"]:
     meijing=(eval(money[1:]))*6.78
     print("&%.2f"%(meijing))
elif money[0] in ["R"]:
    meijing=(eval(money[3:]))/6.78
    print("USD%.2f"%(meijing))
elif money[0] in ["&"]:
    meijing=(eval(money[1:]))/6.78
    print("$%.2f"%(meijing))
else:
    print("Error")



