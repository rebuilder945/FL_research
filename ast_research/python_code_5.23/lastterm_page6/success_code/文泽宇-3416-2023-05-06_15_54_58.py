cnm = input()
if cnm[0]in['&']:
    sb=(eval(cnm[1:]))/6.78
    print("$%.2f"%(sb))
elif cnm[2]in['B']:
    sbb=(eval(cnm[3:]))/6.78
    print("USD%.2f"%(sbb))
elif cnm[0]in['$']:
    sbbb=(eval(cnm[1:]))*6.78
    print("&%.2f"%(sbbb))
elif cnm[2]in['D']:
    sbcnm=(eval(cnm[3:]))*6.78
    print("RMB%.2f"%(sbcnm))
else:
    print('error')
