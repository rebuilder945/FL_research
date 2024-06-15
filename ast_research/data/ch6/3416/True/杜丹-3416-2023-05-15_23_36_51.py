money=input()
if money[0] in ['&']:
    A=eval(money[1:])/6.78
    print("$%.2f"%A)
elif money[0] in ['U']:
    B=eval(money[3:])*6.78
    print("RMB%.2f"%B)
elif money[0 ]in ['$']:
    C=eval(money[1:])*6.78
    print("&%.2f"%C)
elif money[0] in ['R']:
    D=eval(money[3:])/6.78
    print("USD%.2f"%D)
else:
    print("Error")

