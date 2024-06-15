
a=input()
if len(a)!=18:
    print("Error")
else:

    b=list(a[0:17])
    d=[int(i) for i in b]
    c=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    f=sum(d[i]*c[i] for i in range(17))
    g=f%11
    if g==2:
        m='X'
    elif g<2:
        m=1-g
    else:
        m=12-g
    if str(m)==a[-1]:
        print("Correct")
    else:
        print("Wrong")



