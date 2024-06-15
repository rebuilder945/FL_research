a=eval(input())
a.sort(reverse=True)
b=[]
if a[0]==0:
    print("0")
else:
    for i in a:
        i=str(i)
        b.append(i)

    print("".join(b))

