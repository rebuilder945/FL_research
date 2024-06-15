icards=input()
if len(icards)!=18:
    print('Error')
else:
    ls1=list(eval(x) for x in icards[17])
    n=(ls1[0]*7+ls1[1]*9+ls1[2]*10+ls1[3]*5+ls1[4]*8+ls1[5]*4+ls1[6]*2+ls1[7]*1+ls1[8]*6+ls1[9]*3+ls1[10]*7+ls1[11]*9+ls1[12]*10+ls1[13]*5+ls1[14]*8+ls1[15]*4+ls1[16]*2)%11
    m=(12-n)%11
    if str(m)!=icards[-1] and m!=10:
        print('Wrong')
    elif m==10 and icards[-1]=='X':
        print("Correct")
    elif m==10 and icards[-1]!='X':
        print("Wrong")
    elif m!=10 and icards[-1]==str(m):
        print("Correct")
    
