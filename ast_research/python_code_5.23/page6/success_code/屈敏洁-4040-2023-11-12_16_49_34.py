money = input()
if money[0]in['&']:
    USD = eval(money[1:])/6.78 
    print("$%.2f"%(USD))
elif money[0] in['$']:
    RMB = eval(money[1:])*6.78
    print("&%.2f"%(RMB))
elif money[0:3]in['RMB']:
    U = eval(money[3:])/6.78
    print("USD%.2f"%(U))
elif money[0:3] in['USD']:
    R = eval(money[3:])*6.78
    print("RMB%.2f"%(R))
else:        
    print("Error")    

