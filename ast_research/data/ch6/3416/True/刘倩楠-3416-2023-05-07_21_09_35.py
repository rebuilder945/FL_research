CurStr=input()
if CurStr[:3] in ['RMB']:
    U=eval(CurStr[3:])/6.78
    print("USD{:.2f}".format((U)))
elif CurStr[0] in ['&']:
    U=eval(CurStr[1:])/6.78
    print("${:.2f}".format(U))
elif CurStr[:3] in ['USD']:
    R=eval(CurStr[3:])*6.78
    print("RMB{:.2f}".format(R))
elif CurStr[0] in ['$']:
    R=eval(CurStr[1:])*6.78
    print("&{:.2f}".format(R))
else:
    print("Error")

