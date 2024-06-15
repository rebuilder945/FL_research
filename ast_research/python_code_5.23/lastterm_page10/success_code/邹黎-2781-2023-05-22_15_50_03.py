a=input()
total=a[0]*7+a[1]*9+a[2]*10+a[3]*5+a[4]*8+a[5]*4+a[6]*2+a[7]*1+a[8]*6+a[9]*3+a[10]*7+a[11]*9+a[12]*10+a[13]*5+a[14]*8+a[15]*4+a[16]*2
yushu=total%11
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


    
