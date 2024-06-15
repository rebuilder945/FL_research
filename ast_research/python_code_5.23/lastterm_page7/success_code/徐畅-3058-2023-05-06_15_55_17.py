a={}
x=input()
while x!="q":
    if x in a:
        a[x]+=1
    else:
        a[x]=1
    x=input()
else:
    for s in a:
        if a.get(s)==max(a.values()):
            print("{} {}".format(s,a.get(s)))
