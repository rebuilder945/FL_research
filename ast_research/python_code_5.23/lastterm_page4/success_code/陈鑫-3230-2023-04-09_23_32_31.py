a=eval(input())
a.sort()
if a[-1]==0:
    print(0)
else:
    a.reverse()
    a=list(map(str,a))
    print("".join(a))

