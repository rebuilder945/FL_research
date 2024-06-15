currency = input()
if currency[0] in ['$']:
    RMB = eval(currency[1:])*6.78
    print("&%.2f"%RMB)
elif currency[0:3] in ["USD"]:
    RMB = eval(currency[3:])*6.78
    print("RMB%.2f"%RMB)
elif currency[0] in ["&"]:
    USD = eval(currency[1:])/6.78
    print("$%.2f"%USD)
elif currency[0:3] in ["RMB"]:
    USD = eval(currency[3:])/6.78
    print("USD%.2f"%USD)
else:
    print("Error")

