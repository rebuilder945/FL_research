n=input()
a="A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z".split(",")
b="a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z".split(",")
print(n)
n=list(n)
for i in range(len(n)):
    if n[i] in a:
        c=25-a.index(n[i])
        n[i]=a[c]
    elif n[i] in b:
        c=25-b.index(n[i])
        n[i]=b[c]
    else:
        pass
print("".join(n))    




