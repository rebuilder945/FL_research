b = input()
if len(b)==18:
    c = b[0]*7+b[1]*9+b[2]*10+b[3]*5+b[4]*8+b[5]*4+b[6]*2+b[7]+b[8]*6+b[9]*3+b[10]*7+b[11]*9+b[12]*10+b[13]*5+b[14]*8+b[15]*4+b[16]*2
    a = int(c)
    n = a%11
    if n>=0 and n<=10:
        print("Correct")
    else:
        print("Wrong")
else:
    print("Error")
