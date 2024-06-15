a=eval(input())
b="".join(a)
for x in "abcdefghijklmnopqrstuvwxyz":
    if x in b:
        c=a.count(x)
        print(x,",",c)

