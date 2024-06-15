moneystr = input()
if moneystr[0] in ['$']:
    c=(eval(moneystr[1:])*6.78)
    print("&%.2f"%(c))
elif moneystr[0:3] in ['USD']:
    a=(eval(moneystr[3:])*6.78)
    print("RMB%.2f"%(a))
elif moneystr[0] in ['&']:
    b=(eval(moneystr[1:])/6.78)
    print("$%.2f"%(b))
elif moneystr[0:3] in ['RMB']:
   d=(eval(moneystr[3:])/6.78)
   print("USD%.2f"%(d))
else:
    print('Error')
