Money = input()
if Money[0:3] in ['USD']:
    RMB = 6.78*(eval(Money[3:]))
    print("RMB%.2f"%(RMB))
elif Money[0:3] in ['RMB']:
    USD = eval(Money[3:])/6.78
    print("USD%.2f"%(USD))
elif Money[0:1] in ['$']:
    a = 6.78*(eval(Money[1:]))
    print("&%.2f"%a)
elif Money[0:1] in ['&']:
    b = eval(Money[1:])/6.78
    print("$%.2f"%b)
else:
    print("Error")

