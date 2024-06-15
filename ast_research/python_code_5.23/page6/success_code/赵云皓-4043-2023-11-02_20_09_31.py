a=eval(input())
b="".join(a)
for x in "abcdefghijklmnopqrstuvwxyz":
    if x in b:
        c=int(b.count(x))
        d=str(x)
        print("%s,%d"%(d,c))

