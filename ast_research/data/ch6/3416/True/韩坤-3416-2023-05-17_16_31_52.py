daller=input()
if daller[0]in['$']:
    c=eval(daller[1:])*6.78
    print("&%.2f"%(c))
elif daller[0]in['&']:
    yuan2=eval(daller[1:])/6.78
    print("$%.2f"%(yuan2))
elif daller[0]in['R']:
    yuan3=eval(daller[3:])/6.78
    print("USD%.2f"%(yuan3))
elif daller[0]in['U']:
    yuan3=eval(daller[3:])*6.78
    print("RMB%.2f"%(yuan3))
else:
    print("Error")
