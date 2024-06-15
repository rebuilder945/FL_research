a=eval(input())
a.sort()
a.reverse()
if a[0]==0:
    print(0)
else:
    a=list(map(str,a))
    print("".join(a))
