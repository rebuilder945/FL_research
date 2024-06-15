from tkinter import W


a=input()
if len(a)==18:
    b=list(map(int,list(a[:-1])))
    sum=0
    c=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    for x in range(17):
        sum+=b[x]*c[x]
    n=sum%11
    m=(12-n)%11
    if a[-1]=="X":
        c=10
    else:
        c=int(a[-1])
    if c==m:
        print("Correct")
    else:
        print("Wrong")

else:
    print("error")
