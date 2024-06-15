a=list(map(int,input().split(",")))
b=input().split(",")
n=eval(b[0])
m=eval(b[1])
if n<=len(a)-1:
    for i in range(m):
        a.append(a[n])
else:
    print("error")
