huobi = input()
if huobi[0] in ['$']:
    RMB = eval(huobi[1:])/6.78
    print("&%.2f"%(RMB))
elif  huobi[0] in ['USD']:
    RMB = eval(huobi[1:])/6.78
    print("RMB%.2f"%(RMB))
elif huobi[0] in ['&']:
    F = 6.78*eval(huobi[1:]) 
    print("$%.2f"%(F))
elif huobi[0] in ['RMB']:
    F = 6.78*eval(huobi[1:]) 
    print("USD%.2f"%(F))    
else:
    print("Error")
