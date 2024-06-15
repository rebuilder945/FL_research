Money = input()
if Money[0] in ['$']:
    a= eval(Money[1:]) *6.78
    print("&%.2f" % (a))
elif Money[0:3] in ['RMB']:
    b =eval(Money[3:] )/ 6.78
    print("USD%.2f" % (b))
elif Money[0] in ['&']:
    c=eval(Money[1:])/6.78
    print("$%.2f" % (c))
elif Money[0:3] in ['USD']:
    d =eval(Money[3:] )* 6.78
    print("RMB%.2f" % (d))
else:
    print("Error")
