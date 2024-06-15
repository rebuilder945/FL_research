s = input()
if len(s)!=18:
    print("Error")
else:
    b = s[0]*7+s[1]*9+s[2]*10+s[3]*5+s[4]*8+s[5]*4+s[6]*2+s[7]*1+s[8]*6+s[9]*3+s[10]*7+s[11]*9+s[12]*10+s[13]*5+s[14]*8+s[15]*4+s[16]*2
    m = s[-1]
    n = b%11
    if m!="X":
        m = int(m)
        if m ==(12-n)%11:
            print("Correct")
        else:
            print("Wrong")
    else:
        m=10
        if m==(12-n)%11:
            print("Corrrect")
        else:
            print("Wrong")
