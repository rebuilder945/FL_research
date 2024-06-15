Money=input()
if Money[0]in['$']:
    m=eval(Money[1:])*6.78
    print("&%.2f"%m)
elif Money[0]in['&']:
    m=eval(Money[1:])/6.78
    print("$%.2f"%m)
elif Money[0:3]in['USD']:
    m=eval(Money[3:])*6.78
    print("RMB%.2f"%m)
elif Money[0:3]in['RMB']:
    m=eval(Money[3:])/6.78
    print("USD%.2f"%m)
else:
    print("Error")
