a,b =eval(input())
c=[]
if b-a<3 :
    print("illegal input")

else:
    for i in range(a,b):
        c.append(i)
for m,n,p in c:
    if m!=n and n!=p and p!= m:
        c=int(str(m)+str(n)+str(p))
        print(c,end=" ")
    else:
        print("illegal input")


