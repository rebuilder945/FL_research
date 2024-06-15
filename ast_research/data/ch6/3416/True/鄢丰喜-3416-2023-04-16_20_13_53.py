Currency = input()
if Currency[0] in ['R']:
    U = eval(Currency[3:])/6.78
    print("USD%.2f"%(U))
elif Currency[0] in ['&']:
    U = eval(Currency[1:])/6.78
    print("$%.2f"%(U))
elif Currency[0] in ['U']:
    R = 6.78*eval(Currency[3:])
    print("RMB%.2f"%(R))
elif Currency[0] in ['$']:
    R = 6.78*eval(Currency[1:])
    print("&%.2f"%(R))
else:
    print("Error")
    
