a=input()
if len(a)!=18:
    print("Error")
else:
    b=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    s=0
    n=0
    for x in a[:-1]:
        s=s+int(x)*b[n]
        n=n+1
    s=s%11
    m=a[-1]
    if m=="X":
        m="10"
    m=int(m)
    if m==(12-s)%11:
        print("Correct")
    else:
        print("Wrong")

