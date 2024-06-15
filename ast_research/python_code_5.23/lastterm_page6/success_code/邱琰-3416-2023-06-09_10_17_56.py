money=input()
if money[0]=='$':
    r=eval(money[1:])*6.78
    print("&%.2f"%(r))
elif money[0]=='&':
    u=eval(money[1:])/6.78
    print("$%.2f"%(u))
elif money[0:3]=='RMB':
    u=eval(money[3:])/6.78
    print("USD%.2f"%(u))
elif money[0:3]=='USD':
    r=eval(money[3:])*6.78
    print("RMB%.2f"%(r))
else:
    print('Error')
