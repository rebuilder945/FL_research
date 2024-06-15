s=list(input())
a=s[0]*7+s[1]*9+s[2]*10+s[3]*5+s[4]*8+s[5]*4+s[6]*2+s[7]*1+s[8]*6+s[9]*3+s[10]*7+s[11]*9+s[12]*10+s[13]*5+s[14]*8+s[15]*4+s[16]*2
b=a%11
m=(12-b)%11
if len(s)!=18:
    print("Error")
else:
    if m==s[-1]:
        print("Correct")
    else:
        print("Wrong")
