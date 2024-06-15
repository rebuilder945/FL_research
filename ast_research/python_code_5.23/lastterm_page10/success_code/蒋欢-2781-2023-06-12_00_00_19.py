id=input()
if len(id)!=18:
    print("Error")
else:
    sum=int(id[0])*7+9*int(id[1])+10*int(id[2])+5*int(id[3])+8*int(id[4])+4*int(id[5])+2*int(id[6])+int(id[7])+6*int(id[8])+3*int(id[9])+7*int(id[10])+9*int(id[11])+10*int(id[12])+5*int(id[13])+8*int(id[14])+4*int(id[15])+2*int(id[16])
    yu=sum/11
    m=(12-yu)%11
    if m==10:
        m="X"
    else:
        m=str(m)
    if m==id[17]:
        print("Correct")
    else:
        print("Wrong")
