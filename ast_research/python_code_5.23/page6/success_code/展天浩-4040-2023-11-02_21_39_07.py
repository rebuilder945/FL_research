Tempstr=input()
if Tempstr[0]in['$']:
    b=eval(Tempstr[1:])*6.78
    print("&%.2f"%(b))
elif Tempstr[0]in['&']:
    b=eval(Tempstr[1:])/6.78
    print("$%.2f"%(b))
elif Tempstr[:3]in['USD']:
    b=eval(Tempstr[3:])*6.78
    print("RMB%.2f"%(b))
elif Tempstr[:3]in['RMB']:
    b=eval(Tempstr[3:])/6.78
    print("USD%.2f"%(b))    
else:
    print("Error")
