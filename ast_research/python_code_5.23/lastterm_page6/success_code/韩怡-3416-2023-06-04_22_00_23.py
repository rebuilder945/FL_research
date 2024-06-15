Money = input()
if Money[0] in ['&']:
    USD = eval(Money[1:])/6.78
    print("$%.2f"%(USD))
elif Money[0] in ['$']:
    RMB = eval(Money[1:])*6.78
    print("&%.2f"%(RMB))
elif Money[0] in ['R']:
    USD = eval(Money[3:])/6.78
    print("USD%.2f"%(USD))
elif Money[0] in ['U']:
    RMB = eval(Money[3:])*6.78
    print("RMB%.2f"%(RMB))
else:
    print("Error")
