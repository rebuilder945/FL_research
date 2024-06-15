a=eval(input())
a.sort(reverse=True)
c=[str(i) for i in a]
b="".join(c)
d=int(b)
if d>0:
    print(b)
if d==0:
    print("0")
