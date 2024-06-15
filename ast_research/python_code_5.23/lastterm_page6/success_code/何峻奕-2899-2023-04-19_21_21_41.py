n,m=eval(input())
if n>m:
    print("illegal input")
if m-n!=3:
    print("illegal input")
else:
    if n==0:
        print("102 120 201 210")
    if n!=0:
        a=100*n+10*(n+1)+(n+2)
        b=100*n+10*(n+2)+(n+1)
        c=100*(n+1)+10*n+(n+2)
        d=100*(n+1)+10*(n+2)+n
        e=100*(n+2)+10*n+(n+1)
        f=100*(n+2)+10*(n+1)+n
        print(a,b,c,d,e,f)
