a=input()
if len(a)!=18:
    print("Error")
else:
    a=" ".join(a)
    a=a.split()
    for i in range(len(a)-1):
        a[i]=int(a[i])
    b=7*a[0]+9*a[1]+10*a[2]+5*a[3]+8*a[4]+4*a[5]+2*a[6]+a[7]+6*a[8]+3*a[9]+7*a[10]+9*a[11]+10*a[12]+5*a[13]+8*a[14]+4*a[15]+2*a[16]
    n=b%11
    m=(12-n)%11
    if m==10:
        if a[-1]=="X":
            print("Correct")
        else:
            print("Wrong")
    else:
        if str(m)==a[-1]:
            print("Correct")
        else:
            print("Wrong")
