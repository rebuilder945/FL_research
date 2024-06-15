n=input()
ls=[i for i in n]
if len(ls)!=18:
    print('Error')
else:
    for i in range(17):
        ls[i]=int(ls[i])
        sum=ls[0]*7+ls[1]*9+ls[2]*10+ls[3]*5+ls[4]*8+ls[5]*4+ls[6]*2+ls[7]*1+ls[8]*6+ls[9]*3+ls[10]*7+ls[11]*9+ls[12]*10+ls[13]*5+ls[14]*8+ls[15]*4+ls[16]*2
        num=sum%11
        if ls[-1]=='X':
            ls[-1]=10
            if (12-num)%11==ls[-1]:
                print('Correct')
            else:
                print('Wrong')
        else:
            ls[-1]=int(ls[-1])
            if (12-num)%11==ls[-1]:
                print('Correct')
            else:
                print('Wrong')
