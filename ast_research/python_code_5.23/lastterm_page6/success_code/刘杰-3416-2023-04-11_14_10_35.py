M=input()
if M[0] in ['$']:
    N=6.78*eval(M[1:])
    print("&%.2f"%N)
elif M[0] in ['U']:
    N=6.78*eval(M[3:])
    print("RMB%.2f"%N)
elif M[0] in ['&']:
    N=eval(M[1:])/6.78
    print("$%.2f"%N)
elif M[0] in ['R']:
    N=eval(M[3:])/6.78
    print("USD%.2f"%N)
else:
    print("Error")
