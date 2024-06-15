m = input()
if m[:3] in ['RMB']:
    USD = eval(m[3:]) / 6.78
    print("%.2fUSD" % (USD))
elif m[:3] in ['USD', '$']:
    RMB = 6.78 * eval(m[3:])
    print("%.2f" % (RMB))
elif m[:1] in ["&"]:
    a=eval(m[1:]) / 6.78
    print("%.2f$" % (a))
elif m[:1] in ["$"]:
    &= 6.78 * eval(m[1:])
    print("%.2f&" % (&))
else:
    print('Error')


