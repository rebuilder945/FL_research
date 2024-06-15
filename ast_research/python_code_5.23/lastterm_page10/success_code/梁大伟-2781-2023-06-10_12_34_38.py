s=input()
if len(s)==18:
    y=s[-1]
    s1=s[0:17]
    l=list(map(int,s1))
    t=l[0]*7+l[1]*9+l[2]*10+l[3]*5+l[4]*8+l[5]*4+l[6]*2+l[7]*1+l[8]*6+l[9]*3+l[10]*7+l[11]*9+l[12]*10+l[13]*5+l[14]*8+l[15]*4+l[16]*2
    a=t%11
    m=(12-a)%11
    if m==10:
        m='X'
    if m==y:
        print('Correct')
    else:
        print('Wrong')
else:
    print('Error')
