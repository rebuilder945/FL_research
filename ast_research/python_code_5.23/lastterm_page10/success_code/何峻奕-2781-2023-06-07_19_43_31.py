a=input()
m=[]
b=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
sum=0
for i in a:
    m.append(i)
if len(m)!=18:
    print("Error")
else:
    for x in range(17):
        sum=sum+int(m[x])*b[x]
    n=sum%11
    q=(12-n)%11
    if q==m[-1]:
        if q==10:
            X=q
        print("Correct")
    else:
        print("Wrong")
