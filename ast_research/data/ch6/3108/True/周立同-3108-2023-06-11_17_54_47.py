lst=eval(input())
ls=[0]*26
for x in range(len(lst)):
    for y in lst[x]:
        if y=="a":
            ls[0]=ls[0]+1
        if y=="b":
            ls[1]=ls[1]+1
        if y=="c":
            ls[2]=ls[2]+1
        if y=="d":
            ls[3]=ls[3]+1
        if y=="e":
            ls[4]=ls[4]+1
        if y=="f":
            ls[5]=ls[5]+1
        if y=="g":
            ls[6]=ls[6]+1
        if y=="h":
            ls[7]=ls[7]+1
        if y=="i":
            ls[8]=ls[8]+1
        if y=="j":
            ls[9]=ls[9]+1
        if y=="k":
            ls[10]=ls[10]+1
        if y=="l":
            ls[11]=ls[11]+1
        if y=="m":
            ls[12]=ls[12]+1
        if y=="n":
            ls[13]=ls[13]+1
        if y=="o":
            ls[14]=ls[14]+1
        if y=="p":
            ls[15]=ls[15]+1
        if y=="q":
            ls[16]=ls[16]+1
        if y=="r":
            ls[17]=ls[17]+1
        if y=="s":
            ls[18]=ls[18]+1
        if y=="t":
            ls[19]=ls[19]+1
        if y=="u":
            ls[20]=ls[20]+1
        if y=="v":
            ls[21]=ls[21]+1
        if y=="w":
            ls[22]=ls[22]+1
        if y=="x":
            ls[23]=ls[23]+1
        if y=="y":
            ls[24]=ls[24]+1
        if y=="z":
            ls[25]=ls[25]+1
for x in range(len(ls)):
    if ls[x]!=0:
        print(chr(x+97),end="")
        print(",",end="")
        print(ls[x])
