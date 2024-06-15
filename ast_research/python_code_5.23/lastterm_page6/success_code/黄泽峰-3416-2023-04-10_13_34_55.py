M = input()
if M[0] in ['$']:
    C = (eval(M[1:]))*6.78
    print("&%.2f"%C)
elif M[0] in ["U"]:
    c = (eval(M[3:]))*6.78
    print("RMB%.2f"%c)
elif M[0] in ['&']:
    U = (eval(M[1:]))/6.78
    print("$%.2f"%U)
elif M[0] in ["R"]:
    u = (eval(M[3:]))/6.78
    print("USD%.2f"%u)
else:
    print("Error") 

