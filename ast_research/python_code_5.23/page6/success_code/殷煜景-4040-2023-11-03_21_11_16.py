q = input()
if q[0] in ['&']:
    C = eval(q[1:])/6.78
    print("$%.2f"%(C))
elif q[0:3] in ['RMB','rmb']:
    C = eval(q[3:])/6.78
    print("USD%.2f"%(C))
elif q[0] in ['$']:
    F = eval(q[1:])*6.78
    print("&%.2f"%(F))
elif q[0:3] in ['USD','usd']:
    F = eval(q[3:])*6.78
    print("RMB%.2f"%(F))
else:
    print("Error")


