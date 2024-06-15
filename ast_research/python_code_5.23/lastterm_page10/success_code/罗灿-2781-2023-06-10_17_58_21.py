id=input()
if len(id)!=18:
    print('Error')
else:
    sum17=id[0]*7+id[1]*9+id[2]*10+id[3]*5+id[4]*8+id[5]*4+id[6]*2+id[7]*1+id[8]*6+id[9]*3+id[10]*7+id[11]*9+id[12]*10+id[13]*5+id[14]*8+id[15]*4+id[16]*2
    a=int(sum17)
    n=a % 11
    m=(12-n) % 11
    if str(m)!=id[-1] and m!=10:
        print('Wrong')
    elif m==10 and id[-1]=='X':
        print('Correct')
    elif m!=10 and str(m) ==id[-1]:
        print("Correct")
    elif m==10 and id[-1]!="X":
        print("Wrong") 
