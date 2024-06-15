money=input()
if money[0]=="&":
    x=eval(money[1::])/6.78
    print("$%.2f"%x)
elif money[0:3]=="RMB":
    x=eval(money[1::])/6.78
    print("USD%.2f"%x)
elif money[0:3]=="USD":
    x=eval(money[1::])*6.78
    print("RMB%.2f"%x)
elif money[0]=="$":
    x=eval(money[1::])*6.78
    print("&%.2f"%x)
else:
    print("Error")
