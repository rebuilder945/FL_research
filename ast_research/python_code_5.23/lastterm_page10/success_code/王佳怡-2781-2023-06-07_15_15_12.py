a=input()
a1=list(a)
if len(a1)!=18:
    print("Error")
else:
    b=a1[0]*7+a1[1]*9+a1[2]*10+a1[3]*5+a1[4]*8+a1[5]*4+a1[6]*2+a1[7]*1+a1[8]*6+a1[9]*3+a1[10]*7+a1[11]*9+a1[12]*10+a1[13]*5+a1[14]*8+a1[15]*4+a1[16]*2
    n=b%11
    m=a1[-1]
    if m!=X:
        if m==(12-n)%11:
            print("Correct")
        else:
            print("Wrong")
    else:
        m=10
        if m==(12-n)%11:
            print("Correct")
        else:
            print("Wrong")
