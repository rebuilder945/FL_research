sfz = list(input())
if len(sfz) != 18:
    print("Error")
else:
    for i in range(len(sfz)):
        sfz[i] = eval(sfz[i])
    sum = (sfz[0]*7+sfz[1]*9+sfz[2]*10+sfz[3]*5+sfz[4]*8+sfz[5]*4+sfz[6]*2+sfz[7]*1+sfz[8]*6+sfz[9]*3+sfz[10]*7+sfz[11]*9+sfz[12]*10+sfz[13]*5+sfz[14]*8+sfz[15]*4+sfz[16]*2)%11
    m = (12-sum)%11
    if m == 10:
        m = X
    if m == sfz[-1]:
        print("Correct")
    else:
        print("Wrong")
