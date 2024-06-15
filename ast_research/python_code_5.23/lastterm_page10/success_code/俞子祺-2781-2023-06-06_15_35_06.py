n=eval(input())
if len(n)!=18:
    print("Error")
else:
    a=n[0]*7
    b=n[1]*9
    c=n[2]*10
    d=n[3]*5
    e=n[4]*8
    f=n[5]*4
    g=n[6]*2
    h=n[7]*1
    i=n[8]*6
    j=n[9]*3
    k=n[10]*7
    l=n[11]*9
    m=n[12]*10
    o=n[13]*5
    p=n[14]*8
    q=n[15]*4
    r=n[16]*2
    N=(a+b+c+d+e+f+g+h+i+j+k+l+m+o+p+q+r)%11
    M=n[17]
    if M==(12-N)%11:
        print("Correct")
    else:
        print("Wrong")

