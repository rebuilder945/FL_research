a=input()
n,m=eval(input())
d=a.split(",")
if n<len(d):
    b=d[n].split()
    c=d+b*m
    e=list(map(int,c))
    print(e)
else:
    print("error")
