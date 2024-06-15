
a=input()
if len(a)!=18:
    print("Error")
else:

    b=list(a[0:17])
    d=[int(i) for i in b]
    c=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    f=sum(d[i]*c[i] for i in range(17))
    g=f%11
    if g==(0,1,3,4,5,6,7,8,9,10):
        m=(1,0,9,8,7,6,5,4,3,2,1)
    else:
        m=str("x")
    if str(m)==a[-1]:
        print("Corret")
    else:
        print("Wrong")



