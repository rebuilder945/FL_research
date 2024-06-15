a=eval(input())
a.sort(reverse=True)
b=str()
if max(a)>0:
    for x in a:
        x=str(x)
        b+=x
    print(b)
else:
    print("0")
