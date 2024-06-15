M=input()
if M[0] in ['$']:
    Q=eval(M[1:])*6.78
    print("&%.2f"%Q)
elif M[:3] in ['USD']:
    Q=eval(M[3:])*6.78
    print("RMB%.2f"%Q)
elif M[0] in ['&']:
    Q=eval(M[1:])/6.78
    print("$%.2f"%Q)
elif M[:3] in ['RMB']:
    Q=eval(M[3:])/6.78
    print("USD%.2f"%Q)
else:
    print("Error")


