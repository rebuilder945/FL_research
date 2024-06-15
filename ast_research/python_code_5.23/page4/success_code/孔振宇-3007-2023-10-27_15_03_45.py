a=eval(input())
b=input()
c=b.split(",")
d=min(eval(c[0]),eval(c[1]))
e=max(eval(c[0]),eval(c[1]))
if e<=len(a)-1:
    del a[d:e]
    print(a)
else:
    print("error")

