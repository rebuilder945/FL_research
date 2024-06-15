n=list(input())
for i in n:
    if n[i]=='X':
        n[i]='10'
ls=[int(x) for x in n]
if len(n)!=18:
    print('Error')
else:
    a=ls[0]*7+ls[1]*9+ls[2]*10+ls[3]*5+ls[4]*8+ls[5]*4+ls[6]*2+ls[7]*1+ls[8]*6+ls[9]*3+ls[10]*7+ls[11]*9+ls[12]*10+ls[13]*5+ls[14]*8+ls[15]*4+ls[16]*2
    b=a%11
    if ls[-1]==(12-b)%11:
        print('Correct')
    else:
        print('Wrong')
