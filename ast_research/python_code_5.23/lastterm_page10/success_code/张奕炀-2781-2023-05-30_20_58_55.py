number = input()
if len(number) != 18:
    print('Error')
else:
    a=list(map(int,list(number[0:17])))
    sum0=a[0]*7+a[1]*9+a[2]*10+a[3]*5+a[4]*8+a[5]*4+a[6]*2+a[7]*1+a[8]*6+a[9]*3+a[10]*7+a[11]*9+a[12]*10+a[13]*5+a[14]*8+a[15]*4+a[16]*2
    b=sum0%11
    ls=['1','0','X','9','8','7','6','5','4','3','2']
    if ls[b] == number[-1]:
        print('Correct')
    else:
        print('Wrong')
