m=eval(input())
n=list(m)
n.sort(reverse=True)
if n[0]==0:
    print(0)
else:
    for i in n:
        print(i,end="")
