s = input()
if len(s) != 18:
    print("Error")
else:
    ls = [eval(x) for x in s[0:17]]
    sum = ls[0]*7+ls[1]*9+ls[2]*10+ls[3]*5+ls[4]*8+ls[5]*4+ls[6]*2+ls[7]*1+ls[8]*6+ls[9]*3+ls[10]*7+ls[11]*9+ls[12]*10+ls[13]*5+ls[14]*8+ls[15]*4+ls[16]*2
    n = sum%11
    m = (12-n)%11
    if str(m) == s[-1] or (m == 10 and s[-1] == "X"):
        print("Correct")
    else:
        print("Wrong")

