cnm = input()
if cnm[0]in['&']:
    sb=(eval(cnm[1:]))/6.78
    print("$%.2f"%(sb))
elif cnm[0:3]in['RMB']:
    sbb=(eval(cnm[3:]))/6.78
    print("USD%.2f"%(sbb))
elif cnm[0]in['$']:
    sbbb=(eval(cnm[1:]))*6.78
    print("&%.2f"%(sbbb))
elif cnm[0:3]in['USD']:
    sbcnm=(eval(cnm[3:]))*6.78
    print("RMB%.2f"%(sbcnm))
else:
    print('Error')
