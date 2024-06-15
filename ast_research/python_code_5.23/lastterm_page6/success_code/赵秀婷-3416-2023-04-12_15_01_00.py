money=input()
if money[:1]in['$','&']:
    if money[:1]in['$']:
       a=eval(money[1:])*6.78
       print("&%.2f" % (a))
    else:
       b=eval(money[1:])/6.78
       print("$%.2f" % (b))
elif money[:3]in['USD','RMB']:
    if money[:3]in['USD']:
       c=eval(money[3:])*6.78
       print("RMB%.2f" % (c))
    else:
       d=eval(money[3:])/6.78
       print("USD%.2f" % (d))
else:
    print("Error")
