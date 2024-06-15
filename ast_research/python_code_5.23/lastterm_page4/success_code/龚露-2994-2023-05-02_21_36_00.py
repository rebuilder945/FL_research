ls=list(eval(input()))
n,m=eval(input())
r=len(ls)
if abs(int(n))<r and int(n)>0:
    a=0
    while a < int(m):
        ls.append(ls[int(n)])
        a=a+1
    print(ls)
elif abs(int(n))<r and int(n)<0:
    b=0
    while b < int(m):
        ls.append(ls[int(n)+r])
        b=b+1
    print(ls)
else:
    print("error")
