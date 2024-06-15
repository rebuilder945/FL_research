n=input()
m=input()
if n>=m:
    print("illegal input")
if m-n<3:
    print("illegal input")
if m-n>=3:
    lst=[]
    for a in range(n,m):
        for b in range(n,m):
            for c in range(n,m):
                if a!=b and b!=c and c!=a:
                    lst.append(100*a+10*b+c)
    for i in range(len(lst)):
        print(lst[i],end=" ")

