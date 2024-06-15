a=input()
if len(a)==18:
    b=map(int,list(a[:-1]))
    sum=0
    c=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    for x in range(17):
        sum+=b[x]*c[x]
    n=sum%11
    if int(a[-1])==(12-n)%11:
        print("Correct")
    elif (12-n)%11==10 and a[-1]=="X":
        print("Correct")
    else:
        print("Wrong")

