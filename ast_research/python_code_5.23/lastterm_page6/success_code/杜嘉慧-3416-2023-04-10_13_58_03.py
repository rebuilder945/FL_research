Money = eval(input())
if Money[0] in ['$']:
    a= Money[1:] / 6.78
    print("%.2f&" % (a))
elif Money[0:3] in ['RMB']:
    b =Money[3:] / 6.78
    print("%.2fUSD" % (b))
elif Money[0] in ['&']:
    c=Money[1:]*6.78
    print("%.2f$" % (c))
elif Money[0:3] in ['USD']:
    d =Money[3:] * 6.78
    print("%.2fRMB" % (d))
else:
    print("Error")
