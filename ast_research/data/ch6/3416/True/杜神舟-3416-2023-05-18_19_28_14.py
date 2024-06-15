iM = input()
if iM[0] in ['$']:

    im1 = (eval(iM[1:]) )*6.78

    print("&%.2f"%(im1))

elif iM[0:3] in ['USD']:

    im1 = (eval(iM[3:]) )*6.78

    print("RMB%.2f"%(im1))

elif iM[0] in ['&']:

    im2 = eval(iM[1:])/6.78

    print("$%.2f"%(im2))

elif iM[0:3] in ['RMB']:

    im2 = eval(iM[3:])/6.78

    print("USD%.2f"%(im2))

else:

    print("Error")
