a=eval(input())
b=list(a)
n,m=input().split(",")
d=int(n)
f=int(m)
if 0<=d<=len(b)-1 or -len(b)<=d<=-1:
    for i in range(f):
        
        b.append(b[d])
    print(b)
else:
    print("error")

