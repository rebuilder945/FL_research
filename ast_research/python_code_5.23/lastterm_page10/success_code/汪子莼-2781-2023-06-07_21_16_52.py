a=input()
b=list(eval(x) for x in a[:17])
if len(a)!=18:
    print("Error")
else:
    c=b[0]*7+b[1]*9+b[2]*10+b[3]*5+b[4]*8+b[5]*4+b[6]*2+b[7]*1+b[8]*6+b[9]*3+b[10]*7+b[11]*9+b[12]*10+b[13]*5+b[14]*8+b[15]*4+b[16]*2   
    d=c%11
    m=(12-d)%11
    if str(m)!=a[-1] and m!=10:
        print("Wrong")
    elif str(m)==a[-1] and m!=10:
        print("Correct")
    elif m==10 and a[-1]!="X":
        print("wrong")
    elif m==10 and a[-1]=="X":
        print("Correct")
