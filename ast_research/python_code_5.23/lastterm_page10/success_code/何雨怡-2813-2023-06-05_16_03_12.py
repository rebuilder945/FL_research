s=input()
dl=input()
slist=list(s)
new=[]
for i in slist:
    if i!=dl:
        new.append(i)
for x in new:
    print(x,end="")
