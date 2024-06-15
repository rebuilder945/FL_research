c=input().split(" ")
n=eval(c[0])
m=eval(c[1])
if n>m or n<0 or not n==int(n) or not m==int(m) or m-n<3 or n>10:
    print("illegal input")
else:
    d=[]
    for i in range (n,m):
        a=i
        for j in range(n,m):
            b=j
            for k in range(n,m):
                c=k
                if a!=b and a!=0 and a!=c and b!=c:
                    d.append(str(a*100+b*10+c))
print(' '.join(d))



