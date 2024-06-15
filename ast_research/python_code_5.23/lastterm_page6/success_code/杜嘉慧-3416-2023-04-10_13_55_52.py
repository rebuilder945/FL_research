Money = input()
if Money[0] in ['$']:
    a= (eval(Money[1:] / 6.78))
    print("%.2f&" % (a))
elif Money[0:3] in ['RMB']:
    b = (eval(Money[3:] / 6.78))
    print("%.2fUSD" % (b))
elif Money[0] in ['&']:
    c=(eval(Money[1:]*6.78))
    print("%.2f$" % (c))
elif Money[0:3] in ['USD']:
    d = (eval(Money[3:] * 6.78))
    print("%.2fRMB" % (d))
else:
    print("Error")
