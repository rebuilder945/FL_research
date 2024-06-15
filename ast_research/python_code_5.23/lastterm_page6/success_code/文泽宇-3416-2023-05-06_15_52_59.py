cnm = input()
if cnm[0]in['&']:
    sb=(eval(cnm[0:-1]))/6.78
    print("%.2f$"%(sb))
elif cnm[2]in['B']:
    sbb=(eval(cnm[0:-3]))/6.78
    print("%.2fUSD"%(sbb))
elif cnm[0]in['$']:
    sbbb=(eval(cnm[0:-1]))*6.78
    print("%.2f&"%(sbbb))
elif cnm[2]in['D']:
    sbcnm=(eval(cnm[0:-3]))*6.78
    print("%.2fRMB"%(sbcnm))
else:
    print('error')
