a=eval(input())
b=a.sort()
c=b.reverse()
if c[0]==0:
    print(0)
else:
    a=list(map(int,a))
    print("".join(a))
