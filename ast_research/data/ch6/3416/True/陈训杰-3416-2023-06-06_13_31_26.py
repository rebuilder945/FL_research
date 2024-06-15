M=input()
if M[0:3] in ['RMB']:
    D= eval(M[3:])/6.78
    print("USD%.2f" %D)
elif M[0] in ['&']:
    D= eval(M[1:])/6.78
    print("$%.2f" %D)
elif M[0:3] in ['USD']:
    R= eval(M[3:])*6.78
    print("RMB%.2f" %R)
elif M[0] in ['$']:
    R= eval(M[1:])*6.78
    print("&%.2f" %R)
else:
    print("Error")
