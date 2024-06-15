n=input()
if len(n)!=18:
    print("Error")
else:
    s=(7*int(n[0])+9*int(n[1])+10*int(n[2])+5*int(n[3])+8*int(n[4])+4*int(n[5])+2*int(n[6])+int(n[7])+6*int(n[8])+3*int(n[9])+7*int(n[10])+9*int(n[11])+10*int(n[12])+5*int(n[13])+8*int(n[14])+4*int(n[15])+2*int(n[16]))%11
    if s==2:
        if n[17]=='X':
            print("Correct")
        else:
            print("Wrong")
    else:
        if (12-s)%11==n[17]:
            print("Correct")
        else:
            print("Wrong")

