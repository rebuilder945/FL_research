a=(input())
total=(int(a[0]))*7+(int(a[1]))*9+(int(a[2]))*10+(int(a[3]))*5+(int(a[4]))*8+(int(a[5]))*4+(int(a[6]))*2+(int(a[7]))*1+(int(a[8]))*6+(int(a[9])*3+(int(a[10]))*7+(int(a[11]))*9+(int(a[12]))*10+(int(a[13]))*5+(int(a[14]))*8+(int(a[15]))*4+(int(a[16]))*2
yushu=int(total)%11
jieguo=0
if yushu==0:
    jieguo=1
elif yushu==1:
    jieguo=0
elif yushu==2:
    jieguo="X"
else:
    jieguo=12-yushu
if len(a)==18:
    if a[17]==jieguo:
        print("Correct")
    else:
        print("Wrong")
else:
    print("Error")


    
