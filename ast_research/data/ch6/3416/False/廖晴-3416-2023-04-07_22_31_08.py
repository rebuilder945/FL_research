money=input()
if money[-1] in ['$']:
    a=(eval(money[0:-1])*6.78)
    print("%.2f&"%a)
elif money[-1] in ['USD']:
    b=(eval(money[0:-1])*6.78)
    print("%.2fRMB"%b)
elif money[-1] in ['RMB']:
    c=(eval(money[0:-1])//6.78)
    print("%.2fUSD"%c)
elif money[-1] in ['&']:
    d=(eval(money[0:-1])//6.78)
    print("%.2f$"%d)
else:
    print("Error") 
