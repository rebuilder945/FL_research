aMoney = input()
if aMoney[0] in ['$']:
    RMB = (eval(aMoney[1:]))*6.78
    print("&%.2f"%(RMB))
elif aMoney[0:3] in ['USD']:
    RMB = (eval(aMoney[3:]))*6.78
    print("RMB%.2f"%(RMB))
elif aMoney[0] in ['&']:
    USD = (eval(aMoney[1:]))/6.78
    print("$%.2f"%(USD))
elif aMoney[0:3] in ['RMB']:
    USD = (eval(aMoney[3:]))/6.78
    print("USD%.2f"%(USD))
else:
    print("Error")


