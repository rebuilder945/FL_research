m = input()
if m[:3] in ['RMB']:
    USD = eval(m[3:]) / 6.78
    print("USD%.2f" % (USD))
elif m[:3] in ['USD', '$']:
    RMB = 6.78 * eval(m[3:])
    print("RMB%.2f" % (RMB))
elif m[:1] in ["&"]:
    a=eval(m[1:]) / 6.78
    print("$%.2f" % (a))
elif m[:1] in ["$"]:
    b= 6.78 * eval(m[1:])
    print("&%.2f" % (b))
else:
    print('Error')


