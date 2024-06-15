a=eval(input())
b=list(a)
n,m=eval(input())
c=b.copy()
if n>len(b)-1:
    print("error")
else:
    for i in range(m):
        b.append(a[n])
        print(b)
