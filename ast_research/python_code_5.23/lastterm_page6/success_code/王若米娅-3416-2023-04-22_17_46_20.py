str1=input()
if str1[0] in ['&','$']:
    if str1[0]=='&':
        m=eval(str1[1:])/6.78
        print("$%.2f"%m)
    else:
        r=eval(str1[1:])*6.78
        print("&%.2f"%r)
elif str1[:3] in ['USD','RMB']:
    if str1[:3]=='RMB':
        m1=eval(str1[3:])/6.78
        print("USD%.2f"%m1)
    else:
        r1=eval(str1[3:])*6.78
        print("RMB%.2f"%r1)
else:
    print("Error")


