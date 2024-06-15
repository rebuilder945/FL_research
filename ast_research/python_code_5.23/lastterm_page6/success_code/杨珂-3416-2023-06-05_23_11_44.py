huobi = input()
if huobi[0] in ['$']:
    RMB = eval(huobi[1:])*6.78
    print("&%.2f"%(RMB))
elif  huobi[0] in ['U']:
    RMB = eval(huobi[3:])*6.78
    print("RMB%.2f"%(RMB))
elif huobi[0] in ['&']:
    F = eval(huobi[1:])/6.78 
    print("$%.2f"%(F))
elif huobi[0] in ['R']:
    F = eval(huobi[3:])/6.78 
    print("USD%.2f"%(F))    
else:
    print("Error")
