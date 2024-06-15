a=eval(input())
a1=sorted(a,reverse=True)
y=""
if a1[0]==0:
    print(0)
else:
    for i in a1:
        x=str(i)
        y=y+x
    print(y)
