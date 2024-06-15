TempStr = input()
if TempStr[0] in ['$']:
    RMB =  6.78*eval(TempStr[1:])
    print("&%.2f"%(RMB))
elif TempStr[0:3] in ['USD']:
    c =  6.78*eval(TempStr[3:])
    print("RMB%.2f"%(c))
elif TempStr[0] in ['&']:
    USD =(eval(TempStr[1:]))/6.78
    print("$%.2f"%(USD))
elif TempStr[0:3] in ['RMB']:
    a =(eval(TempStr[3:]))/6.78
    print("USD%.2f"%(a))
else:
    print("Error")
