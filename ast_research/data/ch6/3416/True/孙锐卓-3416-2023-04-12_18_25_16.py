MStr=input()
if MStr[0]in['$']:
    RMB=6.78*eval(MStr[1:])
    print("&"'%.2f'%RMB)
elif MStr[:3]in['USD']:
    RMB=6.78*eval(MStr[3:])
    print("RMB"'%.2f'%RMB)
elif MStr[0]in['&']:
    USD=eval(MStr[1:])/6.78
    print("$"'%.2f'%USD)
elif MStr[:3]in['RMB']:
    USD=eval(MStr[3:])/6.78
    print("USD"'%.2f'%USD)
else:
    print("Error")
