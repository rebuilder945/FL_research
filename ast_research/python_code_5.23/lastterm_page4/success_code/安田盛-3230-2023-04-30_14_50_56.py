n=eval(input())
n.sort()
if n[-1]==0:
    print(0)
else:
    t=""
    a=[str(x) for x in n]
    for i in a[::-1]:
        t=t+i
    print(int(t))








