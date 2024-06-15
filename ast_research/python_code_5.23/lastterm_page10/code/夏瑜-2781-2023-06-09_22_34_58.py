a=list(map(int,input())
if len(a)!=18:
    print("Error")
else:
    sum=a[0]*7+a[1]*9+a[2]*10+a[3]*5+a[4]*8+a[5]*4+a[6]*2+a[7]*1+a[8]*6+a[9]*3+a[10]*7+a[11]*9+a[12]*10+a[14]*5+a[15]*8+a[16]*4+a[17]*2
    n=sum%11
    s=['1','0','x','9','8','7','6','5','4','3','2']
    m=s[n]
    if a[-1]==m:
        print('Correct')
    else:
        print('Wrong')





