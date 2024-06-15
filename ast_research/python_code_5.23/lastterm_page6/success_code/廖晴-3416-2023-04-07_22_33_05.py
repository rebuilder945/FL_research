money=input()
if money[0] in ['$']:
    a=(eval(money[-1:0])*6.78)
    print("&%.2f"%a)
elif money[0] in ['USD']:
    b=(eval(money[-1:0])*6.78)
    print("RMB%.2f"%b)
elif money[0] in ['RMB']:
    c=(eval(money[-1:0])//6.78)
    print("USD%.2f"%c)
elif money[0] in ['&']:
    d=(eval(money[-1:0])//6.78)
    print("$%.2f"%d)
else:
    print("Error") 
