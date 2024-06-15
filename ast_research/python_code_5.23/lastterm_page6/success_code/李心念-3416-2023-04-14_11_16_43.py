M = input()
if M[0] in ['&']:
    U1 = eval(M[1:])/6.78
    print("$%.2f"%(U1))

elif M[0:3] in ['RMB']:
    U2 = eval(M[3:])/6.78
    print("USD%.2f"%(U2))

elif M[0] in ['$']:
    R1 = eval(M[1:])*6.78
    print("&%.2f"%(R1))

elif M[0:3] in ['USD']:
    R2 = eval(M[3:])*6.78
    print("RMB%.2f"%(R2))
else:
    print("Error")
