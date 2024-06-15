a=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
b=[0,1,2,3,4,5,6,7,8,9]
c=["1","0","X","9","8","7","6","5","4","3","2"]
s=input()
if len(s)!=18:
    print("Error")
else:
    sum=0
    for i in range(len(s)-1):
        sum+=int(s[i])*a[i]
    d=sum%11
    e=b.index(d)
    if c[e]==s[-1]:
        print("Corrct")
    else:
        print("Wrong")

