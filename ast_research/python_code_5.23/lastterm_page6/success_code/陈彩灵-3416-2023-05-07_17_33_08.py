money = input()

if money[0] =='$':
    C = eval(money[1:])*6.78
    print("&%.2f"%(C))
elif money[0:3]=='USD':
    C = eval(money[3:])*6.78
    print("RMB%.2f"%(C))

elif money[0] =='&':
    F = eval(money[1:])/6.78
    print("$%.2f"%(F))
elif money[0:3] =='RMB':
    F = eval(money[3:])/6.78
    print("USD%.2f"%(F))
else:

    print("Error")
