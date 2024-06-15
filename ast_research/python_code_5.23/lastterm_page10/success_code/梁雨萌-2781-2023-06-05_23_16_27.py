word = input() or 'None'
if len(word) != 18:
    str = 'Error'
    print(str)
else:    
    sym = word[-1::1]
    if sym == 'X':
        sym = 10

    str = word[0:17:1]
    l = [int(x) for x in str]
    sole= l[0]*7 + l[1]*9 + l[2]*10 + l[3]*5 + l[4]*8 + l[5]*4 + l[6]*2 + l[7]*1 +l[8]*6 + l[9]*3 + l[10]*7 + l[11]*9 + l[12]*10 + l[13]*5 + l[14]*8 + l[15]*4 + l[16]*2
    res = sole%11
    m = (12-res)%11
    if m != sym:
        str = 'Wrong'
    else:
        str = 'Correct'
    
print(str)
