a=eval(input())
a.sort(reverse=True)
c=[str(i) for i in a]
b="".join(c)
if b>0:
    print(b)
if b==0:
    print("0")
