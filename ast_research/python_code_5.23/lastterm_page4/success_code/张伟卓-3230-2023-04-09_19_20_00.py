a=eval(input())
a.sort()
if a[-1]==0:
    print(0)
else:
    a=list(map(str,a))
    a.reverse()
    b="".join(a)
    print(b)
