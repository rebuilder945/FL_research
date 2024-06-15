s=input()
if len(s)!=18:
    print("Error")
else:
    b=s[-1]
    a=[int(x) for x in s[0:17]]
    sum=a[0]*7+a[1]*9+a[2]*10+a[3]*5+a[4]*8+a[5]*4+a[6]*2+a[7]*1+a[8]*6+a[9]*3+a[10]*7+a[11]*9+a[12]*10+a[13]*5+a[14]*8+a[15]*4+a[16]*2
    c=sum%11
    m=12-c
    if b=="X":
        b=10
    else:
        b=int(b)
    if b==m:
        print("Correct")
    else:
        print("Wrong")

