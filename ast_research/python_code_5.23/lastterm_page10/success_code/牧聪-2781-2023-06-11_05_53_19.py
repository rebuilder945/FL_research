a=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
b=[int(x) for x in input()]
if len(b)!=18:
    print("Error")
else:
    sum=0
    time=-1
    for i in b[:17]:
        time+=1
        t=i*a[time]
        sum+=t
    n=sum%11
    m=(12-n)%11
    if m==10:
        m="X"
    if m==b[17]:
        print("Correct")
    else:
        print("Wrong")
