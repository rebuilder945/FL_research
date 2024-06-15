money = input()
if money[:1] in ['&','@']:
    RMB1 = (eval(money[1:]))/6.78
    print("$%.2f"%(RMB1))
elif money[:1] in ['$','@']:
    USD1 = 6.78*eval(money[1:])
    print("&%.2f"%(USD1))
elif money[:3] in ['RMB','@']:
    RMB1 = (eval(money[3:]))/6.78
    print("USD%.2f"%(RMB1))
elif money[:3] in ['USD','@']:
    USD1 = 6.78*eval(money[3:])
    print("RMB%.2f"%(USD1))
else:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
    print("Error")

