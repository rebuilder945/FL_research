n,m=eval(input())
if n>m or n<0 or not n==int(n) or not m==int(m) or m-n<3:
    print("illegal input")
else:
    d=[]
    for i in range (n,m):
        a=i
        for j in range(n,m):
            b=j
            for k in range(n,m):
                c=k
                if a!=b!=c and a!=0:
                    d.append(str(a*100+b*10+c))
print(' '.join(d))



