M0=input()
if M0[0] in ['$']:
    M1=(eval(M0[1:])*6.78)
    print("%.2f&"%M1)
elif M0[0] in ['&']:
    M1=(eval(M0[1:])/6.78)
    print("%.2f$"%M1)
elif M0[0:3] in ['USD']:
    M1=(eval(M0[3:])*6.78)
    print("%.2fRMB"%M1)
elif M0[0:3] in ['RMB']:
    M1=(eval(M0[3:])/6.78)
    print("%.2fUSD"%M1)
else:
    print("error")
