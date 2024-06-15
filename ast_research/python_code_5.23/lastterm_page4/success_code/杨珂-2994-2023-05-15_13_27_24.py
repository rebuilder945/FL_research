a=input()
n,m=eval(input())
d=a.split(",")
if n<len(d):
    b=list(int(d[n]))
    c=d+b*m
    e=list(map(int,c))
    print(e,d,a,b)
else:
    print("error")
