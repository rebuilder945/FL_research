c=input()
c1=list(map(int,c[0:-1]))
if len(c)!=18:
    print("Error")
else:
    x=("7-9-10-5-8-4-2-1-6-3-7-9-10-5-8-4-2".split("-"))
    x=list(map(int,x))
    sum=0
    for i in range(0,len(x)):
        sum+=c1[i]*x[i]
    y=sum%11
    y1=list(range(0,11))
    y2=("1-0-X-9-8-7-6-5-4-3-2".split("-"))
    if c[-1]==y2[y]:
        print("Correct")
    else:
        print("Wrong")
