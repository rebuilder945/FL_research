n=[]
end ="q"
for x in iter(input,end):
    n.append(x)
ls=[]
for i in n:
    a=n.count(i)
    ls.append(a)
for x in n:
    if n.count(x)==max(ls):
        print(x,max(ls))
        break
        
