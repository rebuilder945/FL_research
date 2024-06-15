money=input()
if money[0]=="$":
    a=(eval(money[1:])*6.78)
    print("&%.2f"%a)
elif money[0:3]=="USD":
    b=(eval(money[3:])*6.78)
    print("RMB%.2f"%b)
elif money[0:3]=="RMB":
    c=round(eval(money[3:])/6.78+0.001,2)
    print("USD%.2f"%c)
elif money[0]=="&":
    d=round(eval(money[1:])/6.78+0.001,2)
    print("$%.2f"%d)
else:
    print("Error") 
