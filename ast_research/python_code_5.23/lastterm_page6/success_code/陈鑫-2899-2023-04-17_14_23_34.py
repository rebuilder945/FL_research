n=eval(input())
m=eval(input())
e=[]
if n<m and type(n)==type(1) and type(m)==type(1):
    for a in range(n,m):
        for b in range(n,m):
            for c in range(n,m):
                if a!=b and b!=c and a!=c:
                    d=a*100+b*10+c
                    e.append(d)
    if e==[]:
        print("illegal input")
    else:
        print(e)    

else:
    print("illegal input")



