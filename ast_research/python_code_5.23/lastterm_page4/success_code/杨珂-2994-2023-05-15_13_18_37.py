a=input()
n,m=eval(input())
d=a.split(",")
if n<len(a):
    b=list(d[n])
    c=d+b*3
    e=list(map(int,c))
    print(e)
else:
    print("error")
