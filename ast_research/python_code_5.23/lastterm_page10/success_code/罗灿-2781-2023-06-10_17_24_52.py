id=input()
if len(id)!=18:
    print('Error')
else:
    sum17=id[0]*7+id[1]*9+id[2]*10+id[3]*5+id[4]*8+id[5]*4+id[6]*2+id[7]*1+id[8]*6+id[9]*3+id[10]*7+id[11]*9+id[12]*10+id[13]*5+id[14]*8+id[15]*4+id[16]*2
    a=int(sum17)
    n=a % 11
    m=id[17]
    if m=='X':
        m=int(10)
    else:
        m=int(m)

        if m==(12-n)%11:
            print('Correct')
        else:
            print('Wrong')
