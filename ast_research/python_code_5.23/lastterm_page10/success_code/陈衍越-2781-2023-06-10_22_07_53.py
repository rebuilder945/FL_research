sf=input()
l=[]
for i in sf:
    if i=='X':
        i=10
    
    x=int(i)
    l.append(x)
if len(l)!=18:
    print('Error')
else:
    sum=(l[0]*7+l[1]*9+l[2]*10+l[3]*5+l[4]*8+l[5]*4+l[6]*2+l[7]+l[8]*6+l[9]*3+l[10]*7
     +l[11]*9+l[12]*10+l[13]*5+l[14]*8+l[15]*4+l[16]*2)
    ys=sum%11
    m=(12-ys)%11

    if m ==l[17]:
        print('Correct')
    else:
        print('Wrong')

