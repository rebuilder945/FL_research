m=input()
if m[0] in ['$']:
    a=6.78*eval(m[1:])
    print("&%.2f"%(a))
elif m[0] in ['&']:
    b=eval(m[1:])/6.78
    print("$%.2f"%(b))
elif m[0:3] in ['USD']:
    c=6.78*eval(m[3:])
    print("RMB%.2f"%(c))
elif m[0:3] in ['RMB']:
    d=eval(m[3:])/6.78
    print("USD%.2f"%(d))
else:
    print('Error')

