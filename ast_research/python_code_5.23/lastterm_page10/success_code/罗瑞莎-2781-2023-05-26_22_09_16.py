sfz = list(input())
if len(sfz) != 18:
    print("Error")
else:
    for i in range(len(sfz)-1):
        sfz[i] = eval(sfz[i])
    n = (sfz[0]*7+sfz[1]*9+sfz[2]*10+sfz[3]*5+sfz[4]*8+sfz[5]*4+sfz[6]*2+sfz[7]*1+sfz[8]*6+sfz[9]*3+sfz[10]*7+sfz[11]*9+sfz[12]*10+sfz[13]*5+sfz[14]*8+sfz[15]*4+sfz[16]*2)%11
    if n == 2:
        if sfz[-1] == 'X':
            print("Correct")
        else:
            print("Wrong")
    else:
        m = (12-n)%11
        if str(m) == sfz[-1]:
            print("Correct")
        else:
            print("Wrong")
