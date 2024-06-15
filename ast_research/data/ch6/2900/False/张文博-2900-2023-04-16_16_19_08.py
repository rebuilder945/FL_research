def sushu(i):
    x=list(range(2,int(i)))
    j=0
    for k in x:
        if i%k==0:
            j=1
            break
    if j==0:
            return i
def huiwen(i):
    q=list(str(i))
    
    m="".join(q)
    p=q[::-1]
    n="".join(p)
    if p==q:
        return i
    
a=eval(input())
if type(a)==float or a<0:
    print("illegal input")
else:
    b=[r for r in range(2,a+1)]
    c=[]
    for x in b:
        if sushu(x)!=None:
             c.append(x)
    d=[]
    for x in c:
        if huiwen(x)!=None:
            d.append(x)
    for i in d:
        print(i,end=" ")
    
