money=input()
if money[0]=="$":
    b=eval(money[1:])*6.78
    rmb="&"+"%.2f"%(b)
    print(rmb)
elif money[0]=="&":
    b=eval(money[1:])/6.78
    dollar="$"+"%.2f"%(b)
    print(dollar)
elif money[0:3]=="USD":
    b=eval(money[3:])*6.78
    rmb="RMB"+"%.2f"%(b)
    print(rmb)
elif money[0:3]=="RMB":
    b=eval(money[3:])/6.78
    dollar="USD"+"%.2f"%(b)
    print(dollar)
else:
    print("Error")
